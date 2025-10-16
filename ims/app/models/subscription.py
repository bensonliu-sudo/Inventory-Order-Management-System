"""
app/models/subscription.py
Defines the subscription data model for merchants.
"""

from datetime import datetime, timedelta


class Subscription:
    """
    Represents one subscription record.
    """

    def __init__(self, tenant_id: int, plan: str):
        self.tenant_id = tenant_id
        self.plan = plan
        self.start_at = datetime.now()
        self.end_at = self.start_at + (timedelta(days=30) if plan == "monthly" else timedelta(days=365))
        self.status = "ACTIVE"

    def __repr__(self):
        return f"<Subscription tenant={self.tenant_id}, plan={self.plan}, valid_until={self.end_at.date()}>"