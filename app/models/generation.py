import uuid
from sqlalchemy import Column, String, JSON, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base


class Generation(Base):
    __tablename__ = "generations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"))

    status = Column(String, default="processing")

    output = Column(JSON)
    critique = Column(String)

    score = Column(Integer, default=0)