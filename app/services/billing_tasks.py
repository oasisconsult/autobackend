from app.worker.celery_app import celery
from app.db.session import SessionLocal
from app.services.billing_engine import BillingEngine


@celery.task
def run_billing_cycle(user_id: str, tenant_id: str, stripe_customer_id: str):

    db = SessionLocal()

    try:
        engine = BillingEngine()
        return engine.process_user_billing(
            db,
            user_id,
            tenant_id,
            stripe_customer_id
        )

    finally:
        db.close()