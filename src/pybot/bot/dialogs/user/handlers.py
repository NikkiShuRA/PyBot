from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from sqlalchemy.ext.asyncio import AsyncSession

from ....core import logger
from ....services.users import create_user_profile


async def on_first_name_input(
    message: Message,
    widget: MessageInput,
    manager: DialogManager,
) -> None:
    """Обработка ввода имени."""
    first_name: str = message.text.strip() if message.text else ""
    if not first_name:
        await message.answer("❌ Имя не может быть пустым. Попробуйте снова.")
        return

    manager.dialog_data["first_name"] = first_name
    await manager.next()


async def on_last_name_input(
    message: Message,
    widget: MessageInput,
    manager: DialogManager,
) -> None:
    """Обработка ввода фамилии (опционально)."""
    text = message.text.strip() if message.text else ""
    last_name = text if text else None

    manager.dialog_data["last_name"] = last_name
    await manager.next()


async def on_patronymic_input(
    message: Message,
    widget: MessageInput,
    manager: DialogManager,
) -> None:
    """Обработка ввода отчества и создание профиля."""
    text = message.text.strip() if message.text else ""
    patronymic = text if text else None

    dialog_data = manager.dialog_data
    phone: str | None = dialog_data.get("phone")
    tg_id: int | None = dialog_data.get("tg_id")

    if not phone or not tg_id:
        await message.answer("Ошибка: нет данных для создания профиля, попробуй ещё раз /start")
        await manager.done()
        return

    first_name: str | None = dialog_data.get("first_name")

    if first_name is None:
        raise ValueError("Ошибка: нет данных для создания профиля, имя отсуствует.")

    last_name: str | None = dialog_data.get("last_name")

    db: AsyncSession = manager.middleware_data["db"]

    user = await create_user_profile(
        db,
        phone=phone,
        tg_id=tg_id,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
    )
    logger.info(f"Создан user: {user}")
    manager.dialog_data["user_id"] = user.id
    await manager.next()


async def on_patronymic_skip(callback: CallbackQuery, button: Button, manager: DialogManager) -> None:
    dialog_data = manager.dialog_data
    patronymic = None
    phone: str | None = dialog_data.get("phone")
    tg_id: int | None = dialog_data.get("tg_id")

    if not phone or not tg_id:
        await callback.answer("Ошибка: нет данных для создания профиля, попробуй ещё раз /start")
        await manager.done()
        return

    first_name: str | None = dialog_data.get("first_name")

    if first_name is None:
        raise ValueError("Ошибка: нет данных для создания профиля, имя отсуствует.")

    last_name: str | None = dialog_data.get("last_name")

    db: AsyncSession = manager.middleware_data["db"]

    user = await create_user_profile(
        db,
        phone=phone,
        tg_id=tg_id,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
    )
    logger.info(f"Создан user: {user}")
    manager.dialog_data["user_id"] = user.id
