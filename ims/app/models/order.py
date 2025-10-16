"""
app/models/order.py
Defines the structure for customer orders.
"""

from datetime import datetime


class Order:
    """
    Represents a customer's order, linked to tenant and product.
    """

    def __init__(self, order_id: int, tenant_id: int, product_id: int, quantity: int, total_price: float):
        self.id = order_id
        self.tenant_id = tenant_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = round(total_price, 2)
        self.status = "CREATED"
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<Order id={self.id}, tenant={self.tenant_id}, total={self.total_price}, status={self.status}>"