from aiogram.filters import Command
from aiogram.types import Message

from . import global_router


@global_router.message(Command("ping"))
async def cmd_ping(message: Message) -> None:
    await message.answer("pong")
