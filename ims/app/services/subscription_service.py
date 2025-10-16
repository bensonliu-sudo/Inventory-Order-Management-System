"""
app/services/subscription_service.py
Subscription management service for merchants (tenants).

This module simulates how merchants pay the system developer for using
the Inventory Management System (IMS) through subscription plans.
"""

from datetime import datetime, timedelta


class Subscription:
    """
    Data model representing one merchant's subscription record.
    """

    def __init__(self, tenant_id: int, plan: str, start_at: datetime, end_at: datetime):
        self.tenant_id = tenant_id
        self.plan = plan
        self.start_at = start_at
        self.end_at = end_at
        self.status = "ACTIVE"

    def __repr__(self):
        return f"<Subscription tenant={self.tenant_id}, plan={self.plan}, valid_until={self.end_at.date()}>"


class SubscriptionService:
    """
    Handles merchant subscription logic.
    Responsibilities:
      - Create and renew subscriptions
      - Determine if a tenant’s plan is active or expired
      - Compute expiration dates based on plan type
    """

    def __init__(self):
        self.subscriptions = {}  # In-memory "database" for tenant subscriptions

    def renew(self, tenant_id: int, plan: str = "monthly") -> Subscription:
        """
        Renew (or create) a subscription for a tenant.

        Parameters:
            tenant_id (int): The merchant ID.
            plan (str): 'monthly' or 'yearly'.
        """

        # Determine duration
        now = datetime.now()
        if plan == "monthly":
            delta = timedelta(days=30)
        elif plan == "yearly":
            delta = timedelta(days=365)
        else:
            raise ValueError("Unsupported plan type. Use 'monthly' or 'yearly'.")

        # If tenant already has a subscription, extend from existing end date
        if tenant_id in self.subscriptions:
            old_sub = self.subscriptions[tenant_id]
            new_start = old_sub.end_at if old_sub.end_at > now else now
            new_end = new_start + delta
            sub = Subscription(tenant_id, plan, new_start, new_end)
        else:
            sub = Subscription(tenant_id, plan, now, now + delta)

        self.subscriptions[tenant_id] = sub
        print(f"[SubscriptionService] Renewed: {sub}")
        return sub

    def check_status(self, tenant_id: int) -> str:
        """
        Check whether a tenant’s subscription is still active.
        """
        if tenant_id not in self.subscriptions:
            return "NO_SUBSCRIPTION"

        sub = self.subscriptions[tenant_id]
        if datetime.now() > sub.end_at:
            sub.status = "EXPIRED"
        else:
            sub.status = "ACTIVE"

        return sub.status

    def get_subscription(self, tenant_id: int) -> Subscription:
        """Retrieve the tenant's current subscription."""
        if tenant_id not in self.subscriptions:
            raise ValueError(f"No subscription found for tenant {tenant_id}.")
        return self.subscriptions[tenant_id]

    def list_subscriptions(self):
        """List all tenant subscriptions."""
        print("\n=== Subscriptions ===")
        for sub in self.subscriptions.values():
            print(
                f"Tenant {sub.tenant_id}: plan={sub.plan}, valid_until={sub.end_at.date()}, status={sub.status}"
            )
        print("=====================\n")