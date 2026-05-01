from app.models.billing import BillingEvent


class FailureMemory:

    def log_failure(self, db, user_id, failure_type, prompt):

        event = BillingEvent(
            user_id=user_id,
            tenant_id=None,
            event_type="failure",
            tokens_used=0,
            cost_usd=0
        )

        db.add(event)
        db.commit()