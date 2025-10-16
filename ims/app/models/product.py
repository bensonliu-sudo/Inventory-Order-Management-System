"""
app/models/product.py
Defines product and variant models used in the inventory and order systems.
"""

from datetime import datetime


class Product:
    """
    Represents a product (e.g., T-shirt, jacket, etc.)
    """

    def __init__(self, product_id: int, name: str, category: str, price: float):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = round(price, 2)
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<Product id={self.id}, name={self.name}, price={self.price}>"