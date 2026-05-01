from app.models.billing import BillingEvent


class LiveDashboard:

    def get_live_stats(self, db, tenant_id):

        events = db.query(BillingEvent).filter(
            BillingEvent.tenant_id == tenant_id
        ).all()

        return {
            "total_requests": len(events),
            "total_tokens": sum(e.tokens_used for e in events),
            "total_cost": sum(e.cost_usd for e in events)
        }