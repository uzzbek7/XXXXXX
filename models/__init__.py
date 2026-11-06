from .base import Base
from .order import Order
from .order_item import OrderItem
from .product import Product
from .user import User

Orders = Order
Products = Product

__all__ = ["Base", "Order", "OrderItem", "Orders", "Product", "Products", "User"]
