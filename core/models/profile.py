from typing import TYPE_CHECKING

from sqlalchemy import String
from .base import Base
from .mixins import UserRelationMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship


# объявление модели для создания таблицы
class Profile(UserRelationMixin, Base):

    #__tablename__ = 'products'

    # при помощи Mapped указываем что, это будут названия колонок таблицы
    _user_id_unique = True
    _user_back_populates = 'profile'
    first_name: Mapped[str | None] = mapped_column(String(40),unique=False)
    last_name: Mapped[str | None] = mapped_column(String(40),unique=False)
    bio: Mapped[str | None]

