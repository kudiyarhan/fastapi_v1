from .base import Base
from sqlalchemy.orm import Mapped


# объявление модели для создания таблицы
class Product(Base):

    #__tablename__ = 'products'

    # при помощи Mapped указываем что, это будут названия колонок таблицы
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]