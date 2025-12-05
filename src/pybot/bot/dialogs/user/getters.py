from typing import Any

from aiogram_dialog import DialogManager


async def on_profile_start(
    start_data: dict[Any, Any],
    manager: DialogManager,
) -> None:
    # сюда прилетит data из dialog_manager.start(...)
    phone = start_data.get("phone")
    tg_id = start_data.get("tg_id")

    manager.dialog_data["phone"] = phone
    manager.dialog_data["tg_id"] = tg_id
