
from sqlalchemy import String, Text
from .base import Base
from .mixins import UserRelationMixin
from sqlalchemy.orm import Mapped, mapped_column



# объявление модели для создания таблицы
class Post(UserRelationMixin, Base):

    # __tablename__ = 'products'

    # при помощи Mapped указываем что, это будут названия колонок таблицы
    _user_back_populates = 'posts'
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )



