from datetime import datetime, timedelta
from app.models.analytics_event import AnalyticsEvent


class FunnelEngine:

    def get_funnel(self, db, tenant_id):

        events = db.query(AnalyticsEvent).filter(
            AnalyticsEvent.tenant_id == tenant_id
        ).all()

        def count(event_type):
            return len([e for e in events if e.event_type == event_type])

        return {
            "signups": count("signup"),
            "activations": count("activation"),
            "paid_users": count("payment_success"),
            "upgrades": count("upgrade")
        }