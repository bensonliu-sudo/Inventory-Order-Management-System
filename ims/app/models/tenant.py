"""
app/models/tenant.py
Represents a merchant (tenant) that uses the IMS system.
"""


class Tenant:
    """
    A tenant represents a merchant who subscribes to use the IMS system.
    """

    def __init__(self, tenant_id: int, name: str):
        self.id = tenant_id
        self.name = name

    def __repr__(self):
        return f"<Tenant id={self.id}, name={self.name}>"