# tg_bot/handlers/user/profile_create.py
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from .states import ProfileCreate
from services.users import create_user_profile

private_router = Router()
group_router = Router()
global_router = Router()

@private_router.message(ProfileCreate.first_name)
async def profile_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text.strip())
    await message.answer("Фамилия? (можно пропустить, отправив -)")
    await state.set_state(ProfileCreate.last_name)

@private_router.message(ProfileCreate.last_name)
async def profile_last_name(message: Message, state: FSMContext):
    text = message.text.strip()
    last_name = None if text == "-" else text
    await state.update_data(last_name=last_name)
    await message.answer("Отчество? (можно пропустить, отправив -)")
    await state.set_state(ProfileCreate.patronymic)

@private_router.message(ProfileCreate.patronymic)
async def profile_patronymic(message: Message, state: FSMContext, db: AsyncSession):
    text = message.text.strip()
    patronymic = None if text == "-" else text

    data = await state.get_data()
    phone: str = data["phone"]
    tg_id: int = data["tg_id"]
    first_name: str = data["first_name"]
    last_name: str | None = data["last_name"]

    user = await create_user_profile(
        db,
        phone=phone,
        tg_id=tg_id,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
    )

    await state.clear()
    await message.answer(
        f"Профиль создан. Твой ID: {user.id}"
    )
