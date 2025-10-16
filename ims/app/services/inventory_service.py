"""
 Business logic layer for managing inventory items.
 This service controls stock levels of product variants.
 It simulates a database using in-memory data structures
 and provides basic operations such as adding, reducing,
 and checking stock quantities.

"""

from datetime import datetime


class InventoryItem:
    """
    Data model representing one product variant in inventory.
    In a real system, this would correspond to a database table.
    """

    def __init__(self, variant_id: int, name: str, stock: int = 0):
        self.variant_id = variant_id
        self.name = name
        self.stock = stock
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<InventoryItem id={self.variant_id}, name={self.name}, stock={self.stock}>"

    def adjust(self, quantity: int):
        """Increase or decrease stock quantity."""
        self.stock += quantity
        self.updated_at = datetime.now()


class InventoryService:
    """
    Core service responsible for managing stock quantities.

    Responsibilities:
      - Add new inventory items
      - Adjust existing stock levels
      - Query current stock
      - Validate inventory availability for orders
    """

    def __init__(self):
        # Simulate a simple in-memory "database"
        # Key: variant_id, Value: InventoryItem
        self.items = {}

        # Preload one default item for demo purposes
        default_item = InventoryItem(variant_id=101, name="Classic White T-Shirt", stock=0)
        self.items[default_item.variant_id] = default_item

    # Inventory CRUD (Core Methods)

    def add_item(self, variant_id: int, name: str, initial_stock: int = 0):
        """Register a new inventory item."""
        if variant_id in self.items:
            raise ValueError(f"Variant {variant_id} already exists in inventory.")
        item = InventoryItem(variant_id=variant_id, name=name, stock=initial_stock)
        self.items[variant_id] = item
        print(f"[Inventory] Added item: {item}")
        return item

    def adjust_stock(self, variant_id: int, quantity: int) -> int:
        """
        Adjust stock quantity for an existing item.
        Positive quantity → Add stock
        Negative quantity → Deduct stock
        """
        if variant_id not in self.items:
            raise ValueError(f"Variant {variant_id} not found in inventory.")

        item = self.items[variant_id]
        new_stock = item.stock + quantity
        if new_stock < 0:
            raise ValueError(f"Insufficient stock for variant {variant_id}. Current: {item.stock}")

        item.adjust(quantity)
        return item.stock

    def get_stock(self, variant_id: int) -> int:
        """Return the current stock level of an item."""
        if variant_id not in self.items:
            raise ValueError(f"Variant {variant_id} not found.")
        return self.items[variant_id].stock

    def list_all_items(self):
        """Return all inventory records (for admin/debug)."""
        print("\n=== Current Inventory ===")
        for item in self.items.values():
            print(f"ID: {item.variant_id}, Name: {item.name}, Stock: {item.stock}")
        print("==========================\n")

 
    # Utility for Testing

    def reset_inventory(self):
        """Reset all stock quantities (used in tests)."""
        for item in self.items.values():
            item.stock = 0
        print("[Inventory] All stock reset to 0.")