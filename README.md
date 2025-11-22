# PyBot

PyBot — лёгкий асинхронный Telegram‑бот на Python, использующий `aiogram` и асинхронную базу данных.

Этот репозиторий содержит реализацию бота с модульной структурой: обработчики, сервисы и слой доступа к базе данных.

Основные возможности
- Отправка/обработка сообщений через `aiogram` (polling)
- Асинхронная работа с базой данных через SQLAlchemy + `asyncpg`
- Модульная структура: `handlers`, `services`, `db_class`, `models`

Быстрый старт
1. Склонируйте репозиторий и перейдите в папку проекта:

```powershell
git clone <repo-url>
cd PyBot
```

2. Создайте виртуальное окружение и активируйте его (Windows PowerShell):

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

3. Установите зависимости (рекомендуемые пакеты):

```powershell
pip install aiogram sqlalchemy[asyncio] asyncpg python-dotenv
```

4. Создайте файл `.env` в корне проекта и заполните переменные окружения (пример ниже):

```
BOT_TOKEN_TEST=123456:ABC-DEF
DB_USER=postgres
DB_PASS=secret
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pybot_db
```

5. Запустите бота:

```powershell
python run.py
```

Что нужно знать о проекте
- Точка входа: `run.py` — инициализирует БД (`init_db()`), создаёт `Bot` и `Dispatcher`, подключает middleware с сессией БД и запускает polling.
- Конфигурация: `config.py` читает переменные окружения (использует `python-dotenv`).
- Слой БД: папка `db_class` содержит логику инициализации и сессии БД; `models/` хранит модели по модулям (пользователи, проекты, задачи и т.п.).
- Обработчики: `handlers/` содержит маршруты (router), пример — `handlers/test.py`.
- Сервисы: `services/` инкапсулируют бизнес-логику (например, `users.py`, `attachment.py`).

Структура проекта (сокращённо)

```
README.md
run.py
config.py
db_class/
	database.py
	base_class.py
models/
	... (user_module, task_module, project_module и т.д.)
handlers/
	test.py
services/
	users.py
	attachment.py
tg_bot/
```

Переменные окружения
- `BOT_TOKEN_TEST` — токен Telegram-бота для тестового окружения.
- `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_PORT`, `DB_NAME` — параметры подключения к Postgres (используется строка в `config.py`).

Дальнейшие шаги
- Написать логику бота (развитие handlers и service).
- Создать `requirements.txt` или `pyproject.toml` для фиксации зависимостей.
- Добавить `.env.example` с описанием переменных окружения (без секретов).
- Написать простые интеграционные/юнит‑тесты для основных обработчиков и сервисов.
- Добавить Dockerfile / docker‑compose для удобного запуска Postgres + бота.

Лицензия MIT
Проект содержит файл `LICENSE` в корне репозитория.

