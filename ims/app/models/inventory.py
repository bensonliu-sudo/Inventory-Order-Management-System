"""
app/models/inventory.py
Represents stock and product variants for inventory tracking.
"""


class StockItem:
    """
    Represents a single item in the warehouse inventory.
    """

    def __init__(self, variant_id: int, product_id: int, quantity: int):
        self.variant_id = variant_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"<StockItem variant={self.variant_id}, product={self.product_id}, qty={self.quantity}>"