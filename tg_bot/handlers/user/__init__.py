# tg_bot/handlers/user/__init__.py
from aiogram import Router, F

from . import profile_create, states

# Роутер для личных чатов
private_router = Router()
private_router.message.filter(F.chat.type == "private")

# Роутер для групп/супергрупп
group_router = Router()
group_router.message.filter(F.chat.type.in_({"group", "supergroup"}))

# Роутер для всех типов чатов
global_router = Router()
global_router.message.filter(F.chat.type.in_({"private", "group", "supergroup"}))


# Подключаем хендлеры
private_router.include_router(profile_create.private_router)

group_router.include_router(profile_create.group_router)

global_router.include_router(profile_create.global_router)