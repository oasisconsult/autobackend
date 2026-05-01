from app.db.session import SessionLocal
from app.models.tenant import Tenant


def seed():
    db = SessionLocal()

    tenant = Tenant(name="Demo Tenant")

    db.add(tenant)
    db.commit()

    print("Seeded demo tenant")