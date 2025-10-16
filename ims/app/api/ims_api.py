"""
 The main API orchestrator for the Inventory Management System (IMS).

 This layer simulates REST-style business endpoints. In a real web app,
 it would be implemented using FastAPI or Flask routes. Here, we provide
 the same logical flow via plain Python classes for demonstration.

 Key responsibilities:
   - Coordinate services (Inventory, Order, Payment, Subscription)
   - Expose unified methods for each business operation
   - Provide a full demo_flow() for end-to-end process simulation

 Author : Bingcheng Liu
 Version: v1.0 Demo Architecture Edition
"""

from datetime import datetime
from app.services.inventory_service import InventoryService
from app.services.order_service import OrderService
from app.services.payment_service import PaymentService
from app.services.subscription_service import SubscriptionService


class IMSApi:
    """
    Main orchestration class for the Inventory Management System.
    Handles all business workflows by delegating to service modules.
    """

    def __init__(self):
        """
        Initialize all service instances.
        Each service has its own business logic and internal data store.
        """
        self.inventory_service = InventoryService()
        self.order_service = OrderService(self.inventory_service)
        self.payment_service = PaymentService()
        self.subscription_service = SubscriptionService()

    # Inventory API Simulation
    def add_stock(self, variant_id: int, qty: int):
        """
        Add stock to an existing inventory item.
        This simulates an API endpoint:
            POST /inventory/add
        """
        new_qty = self.inventory_service.adjust_stock(variant_id, qty)
        print(f"[Inventory] Variant {variant_id} stock adjusted to {new_qty}")
        return {"variant_id": variant_id, "new_qty": new_qty}

    def reduce_stock(self, variant_id: int, qty: int):
        """
        Reduce stock after an order is placed.
        """
        new_qty = self.inventory_service.adjust_stock(variant_id, -qty)
        print(f"[Inventory] Variant {variant_id} stock adjusted to {new_qty}")
        return {"variant_id": variant_id, "new_qty": new_qty}

    # Order API Simulation
    def create_order(self, tenant_id: int, items: list):
        """
        Create a new order for a tenant (merchant).
        In a real REST API, this would be:
            POST /orders
        """
        order = self.order_service.create_order(tenant_id, items)
        print(f"[Order Created] ID={order.id}")
        return {"order_id": order.id, "tenant_id": tenant_id, "status": order.status}
    # Payment API Simulation
    def pay_order(self, tenant_id: int, order_id: int, amount: float, method: str = "cash"):
        """
        Record a payment for an order.
        In a real system, this could connect to Stripe, Alipay, etc.
        """
        payment = self.payment_service.pay_order(tenant_id, order_id, amount, method)
        print(f"[Payment Completed] Order {order_id} paid {amount} USD via {method}")
        return {
            "payment_id": payment.id,
            "order_id": order_id,
            "amount": payment.amount,
            "method": payment.method,
            "status": payment.status
        }

    # Subscription API Simulation
    def renew_subscription(self, tenant_id: int, plan: str = "monthly"):
        """
        Renew merchant’s subscription plan.
        In production, this might trigger a billing API.
        """
        subscription = self.subscription_service.renew(tenant_id, plan)
        print(
            f"[Subscription Renewed] Tenant {tenant_id} renewed {plan} plan, "
            f"valid until {subscription.end_at.date()}"
        )
        return {
            "tenant_id": tenant_id,
            "plan": plan,
            "valid_until": str(subscription.end_at.date())
        }

    # Full Demonstration Workflow
    def demo_flow(self):
        """
        Demonstrate the complete IMS process:
          1. Add stock
          2. Create order
          3. Process payment
          4. Renew subscription
        """
        print("======== IMS System Demonstration ========")

        # Step 1: Add stock
        print("\n[STEP 1] Adding stock ...")
        self.add_stock(variant_id=101, qty=100)

        # Step 2: Create order
        print("\n[STEP 2] Creating order ...")
        order_result = self.create_order(
            tenant_id=1,
            items=[{"variant_id": 101, "qty": 2, "price": 99.9}]
        )

        # Reduce stock after order
        self.reduce_stock(variant_id=101, qty=2)

        # Step 3: Pay for order
        print("\n[STEP 3] Processing payment ...")
        self.pay_order(tenant_id=1, order_id=order_result["order_id"], amount=199.8)

        # Step 4: Renew subscription
        print("\n[STEP 4] Renewing subscription ...")
        self.renew_subscription(tenant_id=1, plan="monthly")

        print("\n======== Demonstration Completed ========\n")