"""
app/services/payment_service.py
Payment service for handling customer transactions.
This module simulates payments from customers to merchants.
"""

from datetime import datetime


class Payment:
    """
    Data model representing one payment transaction.
    """

    def __init__(self, payment_id: int, tenant_id: int, order_id: int, amount: float, method: str):
        self.id = payment_id
        self.tenant_id = tenant_id
        self.order_id = order_id
        self.amount = amount
        self.method = method
        self.status = "COMPLETED"
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<Payment id={self.id}, order={self.order_id}, amount={self.amount}, method={self.method}>"


class PaymentService:
    """
    Business logic layer for handling order payments.
    Responsibilities:
      - Record customer payments
      - Validate payment amounts
      - Simulate payment status (success, failed, refunded)
    """

    def __init__(self):
        self.payments = {}  # In-memory database of payment records
        self.next_id = 1

    def pay_order(self, tenant_id: int, order_id: int, amount: float, method: str = "cash") -> Payment:
        """
        Process a payment for a given order.
        In a real system, this could integrate with Alipay, WeChat Pay, Stripe, etc.
        """

        # Basic validation
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")

        # Simulate payment creation
        payment = Payment(
            payment_id=self.next_id,
            tenant_id=tenant_id,
            order_id=order_id,
            amount=round(amount, 2),
            method=method
        )

        self.payments[self.next_id] = payment
        self.next_id += 1

        print(f"[PaymentService] Payment recorded: {payment}")
        return payment

    def get_payment(self, payment_id: int) -> Payment:
        """Retrieve a specific payment by ID."""
        if payment_id not in self.payments:
            raise ValueError(f"Payment ID {payment_id} not found.")
        return self.payments[payment_id]

    def list_payments(self):
        """List all recorded payments."""
        print("\n=== Payment Records ===")
        for p in self.payments.values():
            print(f"Payment {p.id}: order={p.order_id}, amount={p.amount}, method={p.method}, status={p.status}")
        print("=======================\n")

    def refund_payment(self, payment_id: int):
        """Mark a payment as refunded."""
        payment = self.get_payment(payment_id)
        if payment.status != "COMPLETED":
            raise ValueError("Only completed payments can be refunded.")
        payment.status = "REFUNDED"
        print(f"[PaymentService] Payment {payment_id} has been refunded.")