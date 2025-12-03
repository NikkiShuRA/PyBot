from pydantic import Field, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    """Конфигурация бота с валидацией и типизацией"""

    # Telegram settings
    bot_token: str = Field(..., alias="BOT_TOKEN", description="Токен тестового бота")

    # Database settings
    db_user: str = Field(..., alias="DB_USER", description="Пользователь PostgreSQL")
    db_pass: str = Field(..., alias="DB_PASS", description="Пароль PostgreSQL")
    db_host: str = Field("localhost", alias="DB_HOST", description="Хост PostgreSQL")
    db_port: int = Field(5432, alias="DB_PORT", description="Порт PostgreSQL")
    db_name: str = Field(..., alias="DB_NAME", description="Имя базы данных")

    database_url: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    @field_validator("database_url", mode="before")
    def assemble_db_url(cls, v: str | None, info: ValidationInfo) -> str:  # noqa: N805
        """Автоматически формирует URL для подключения к БД"""
        if v:
            return v

        values = info.data
        return (
            f"postgresql+asyncpg://"
            f"{values['db_user']}:{values['db_pass']}@"
            f"{values['db_host']}:{values['db_port']}/"
            f"{values['db_name']}"
        )


settings: BotSettings = BotSettings()
