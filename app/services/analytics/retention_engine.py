from datetime import datetime, timedelta
from app.models.analytics_event import AnalyticsEvent


class RetentionEngine:

    def get_retention(self, db, tenant_id, days=30):

        events = db.query(AnalyticsEvent).filter(
            AnalyticsEvent.tenant_id == tenant_id,
            AnalyticsEvent.event_type == "login"
        ).all()

        now = datetime.utcnow()

        cohorts = {
            "day_1": 0,
            "day_7": 0,
            "day_30": 0
        }

        for e in events:

            diff = (now - e.created_at).days

            if diff <= 1:
                cohorts["day_1"] += 1
            if diff <= 7:
                cohorts["day_7"] += 1
            if diff <= 30:
                cohorts["day_30"] += 1

        return cohorts