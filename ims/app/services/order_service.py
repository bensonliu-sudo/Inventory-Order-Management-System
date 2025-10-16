"""
 app/services/order_service.py
 Business logic layer for handling orders.

 This module defines the Order data model and manages order creation,
 validation, and linking with inventory changes.

 Author : Bingcheng Liu
 Version: v1.0 Demo Architecture Edition
"""

from datetime import datetime
from typing import List, Dict
from app.services.inventory_service import InventoryService


class OrderItem:
    """
    Represents a single product line inside an order.
    """
    def __init__(self, variant_id: int, qty: int, price: float):
        self.variant_id = variant_id
        self.qty = qty
        self.price = price

    @property
    def subtotal(self) -> float:
        """Calculate subtotal for this line."""
        return round(self.qty * self.price, 2)

    def __repr__(self):
        return f"<OrderItem variant={self.variant_id}, qty={self.qty}, price={self.price}>"


class Order:
    """
    Order entity representing one purchase record.

    Real systems would persist this to a database and include
    more states such as 'shipped', 'cancelled', etc.
    """

    def __init__(self, order_id: int, tenant_id: int, items: List[OrderItem]):
        self.id = order_id
        self.tenant_id = tenant_id
        self.items = items
        self.status = "CREATED"
        self.created_at = datetime.now()
        self.total_amount = self.calculate_total()

    def calculate_total(self) -> float:
        """Sum all line subtotals."""
        return round(sum(item.subtotal for item in self.items), 2)

    def __repr__(self):
        return f"<Order id={self.id}, tenant={self.tenant_id}, total={self.total_amount}>"


class OrderService:
    """
    Service responsible for order creation and inventory synchronization.

    Responsibilities:
      - Validate and create new orders
      - Deduct inventory quantities after order confirmation
      - Manage order status transitions
    """

    def __init__(self, inventory_service: InventoryService):
        # Dependency injection — inventory service is shared
        self.inventory_service = inventory_service

        # Internal "database" of orders
        self.orders: Dict[int, Order] = {}
        self.next_id = 1  # Auto-increment simulation

    # Core Business Logic
    def create_order(self, tenant_id: int, items: List[Dict]) -> Order:
        """
        Create an order for a tenant (merchant).

        Parameters:
          tenant_id (int): The merchant placing the order
          items (list): A list of dicts like:
                [{"variant_id": 101, "qty": 2, "price": 99.9}]
        """

        # Step 1. Convert input dicts → OrderItem objects
        order_items = [OrderItem(**i) for i in items]

        # Step 2. Validate inventory availability
        for item in order_items:
            stock = self.inventory_service.get_stock(item.variant_id)
            if stock < item.qty:
                raise ValueError(
                    f"Insufficient stock for variant {item.variant_id}. "
                    f"Available: {stock}, Required: {item.qty}"
                )

        # Step 3. Deduct inventory
        for item in order_items:
            self.inventory_service.adjust_stock(item.variant_id, -item.qty)

        # Step 4. Create order record
        order = Order(order_id=self.next_id, tenant_id=tenant_id, items=order_items)
        self.orders[self.next_id] = order
        self.next_id += 1

        print(f"[OrderService] Created {order}")
        return order

    def get_order(self, order_id: int) -> Order:
        """Retrieve an order by ID."""
        if order_id not in self.orders:
            raise ValueError(f"Order ID {order_id} not found.")
        return self.orders[order_id]

    def list_orders(self):
        """List all orders for debugging/demo."""
        print("\n=== All Orders ===")
        for order in self.orders.values():
            print(f"Order {order.id}: total={order.total_amount}, status={order.status}")
        print("===================\n")

    def cancel_order(self, order_id: int):
        """Cancel an existing order and restore inventory."""
        order = self.get_order(order_id)
        if order.status != "CREATED":
            raise ValueError("Only newly created orders can be cancelled.")
        for item in order.items:
            self.inventory_service.adjust_stock(item.variant_id, item.qty)
        order.status = "CANCELLED"
        print(f"[OrderService] Order {order_id} cancelled and stock restored.")