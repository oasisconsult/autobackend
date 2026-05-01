from app.models.billing import BillingEvent
from app.services.cost_calculator import CostCalculator


class BillingTracker:

    def __init__(self):
        self.calc = CostCalculator()

    def track_generation(self, db, user_id, tenant_id, tokens):

        cost = self.calc.calculate_total(tokens)

        event = BillingEvent(
            user_id=user_id,
            tenant_id=tenant_id,
            event_type="generation",
            tokens_used=tokens,
            cost_usd=cost
        )

        db.add(event)
        db.commit()

        return event
    
def track_request(self, db, user_id, tenant_id):

    event = BillingEvent(
        user_id=user_id,
        tenant_id=tenant_id,
        event_type="request",
        tokens_used=0,
        cost_usd=0
    )

    db.add(event)
    db.commit()