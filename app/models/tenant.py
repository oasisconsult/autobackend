import uuid
from sqlalchemy import Column, String
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)