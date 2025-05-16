# указываем что все идет на экспорт
__all_ = (
    "Base",
    'DatabaseHelper', 
    'db_helper',
    'Product'
)
from .base import Base
from .db_helper import DatabaseHelper, db_helper
from .product import Product

