from sqlalchemy import String, Text, ForeignKey
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


# объявление модели для создания таблицы
class Post(Base):

    # __tablename__ = 'products'

    # при помощи Mapped указываем что, это будут названия колонок таблицы
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
