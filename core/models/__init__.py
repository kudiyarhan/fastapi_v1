# указываем что все идет на экспорт
__all_ = (
    "Base",
    'DatabaseHelper', 
    'db_helper',
    'Product',
    'User',
    'Post',
)
from .base import Base
from .db_helper import DatabaseHelper, db_helper
from .product import Product
from .user import User
from .post import Post

