import uuid
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base


class TenantSubscription(Base):
    __tablename__ = "tenant_subscriptions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"))
    plan_id = Column(UUID(as_uuid=True), ForeignKey("plans.id"))

    stripe_customer_id = Column(String)
    status = Column(String, default="active")