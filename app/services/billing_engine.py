from app.services.stripe_service import StripeService
from app.models.billing import BillingEvent


class BillingEngine:

    def __init__(self):
        self.stripe = StripeService()

    def process_user_billing(self, db, user_id, tenant_id, stripe_customer_id):

        events = db.query(BillingEvent).filter(
            BillingEvent.user_id == user_id,
            BillingEvent.stripe_invoiced == "pending"
        ).all()

        total = sum(e.cost_usd for e in events)

        if total <= 0:
            return {"status": "no charges"}

        # push to Stripe
        self.stripe.create_usage_invoice(stripe_customer_id, total)
        self.stripe.finalize_invoice(stripe_customer_id)

        # mark as billed
        for e in events:
            e.stripe_invoiced = "paid"

        db.commit()

        return {
            "status": "billed",
            "amount": total
        }