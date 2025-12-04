from aiogram import Router, F

private_router = Router()
private_router.message.filter(F.chat.type == "private")

# Роутер для групп/супергрупп
group_router = Router()
group_router.message.filter(F.chat.type.in_({"group", "supergroup"}))

# Роутер для общих команд (например, /info) можно оставить, но будьте осторожны
global_router = Router()

# from . import common
