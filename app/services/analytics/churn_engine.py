from datetime import datetime, timedelta


class ChurnEngine:

    def detect_risk(self, user_events):

        last_event = max(user_events, key=lambda x: x.created_at, default=None)

        if not last_event:
            return "HIGH_RISK"

        days_inactive = (datetime.utcnow() - last_event.created_at).days

        if days_inactive > 3:
            return "HIGH_RISK"

        if days_inactive > 7:
            return "CRITICAL_RISK"

        return "LOW_RISK"