import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base


class BillingEvent(Base):
    __tablename__ = "billing_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"))

    event_type = Column(String)  # generation, validation, zip_download
    tokens_used = Column(Integer, default=0)

    cost_usd = Column(Float, default=0.0)

    stripe_invoiced = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)