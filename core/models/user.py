from sqlalchemy import String
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


# объявление модели для создания таблицы
class User(Base):

    #__tablename__ = 'products'

    # при помощи Mapped указываем что, это будут названия колонок таблицы
    username: Mapped[str] = mapped_column(String(32),unique=True)
