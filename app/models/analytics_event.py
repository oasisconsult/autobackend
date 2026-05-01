import uuid
from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base


class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(UUID(as_uuid=True))
    user_id = Column(UUID(as_uuid=True))

    event_type = Column(String)  # signup, activation, generation, upgrade, churn_risk
    metadata = Column(JSON, default={})

    created_at = Column(DateTime, default=datetime.utcnow)