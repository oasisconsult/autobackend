import uuid
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base


class Plan(Base):
    __tablename__ = "plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, unique=True)

    # quotas
    max_requests_per_minute = Column(Integer, default=10)
    max_tokens_per_day = Column(Integer, default=10000)
    max_generations_per_day = Column(Integer, default=10)

    # pricing
    base_price = Column(Float, default=0.0)