from pathlib import Path # указываем абсолютный путь для создания таблицы
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent # указываем абсолютный путь для создания таблицы


class Settings(BaseSettings):
    api_v1_prefix: str = '/api/v1'

    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'
    db_echo: bool = True

settings = Settings()