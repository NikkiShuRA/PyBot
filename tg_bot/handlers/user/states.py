# tg_bot/handlers/user/states.py
from aiogram.fsm.state import StatesGroup, State

class ProfileCreate(StatesGroup):
    first_name = State()
    last_name = State()
    patronymic = State()
