"""
app/tests/test_demo_flow.py
End-to-end test simulating a full flow: inventory -> order -> payment -> subscription
"""

from app.services.inventory_service import InventoryService
from app.services.order_service import OrderService
from app.services.payment_service import PaymentService
from app.services.subscription_service import SubscriptionService


def run_demo():
    print("\n===== IMS Demo Test =====")

    inventory = InventoryService()
    order = OrderService(inventory)
    payment = PaymentService()
    sub = SubscriptionService()

    # Step 1: Add stock
    inventory.adjust_stock(variant_id=101, delta=10)

    # Step 2: Create an order
    order_obj = order.create_order(tenant_id=1, product_id=101, quantity=2, price_per_unit=50.0)

    # Step 3: Payment
    pay_obj = payment.pay_order(tenant_id=1, order_id=order_obj.id, amount=order_obj.total_price, method="cash")

    # Step 4: Subscription renewal
    sub.renew(tenant_id=1, plan="monthly")

    print("\n===== Demo Completed Successfully =====\n")


if __name__ == "__main__":
    run_demo()