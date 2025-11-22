import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram import F

from config import BOT_TOKEN
from db_class.database import SessionLocal, init_db
from handlers import test as start_handlers


# простейший middleware для сессии БД
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any


class DbSessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        async with SessionLocal() as session:
            data["db"] = session
            return await handler(event, data)


async def main():
    await init_db()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.message.middleware(DbSessionMiddleware())

    dp.include_router(start_handlers.router)

    # сбросить накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
