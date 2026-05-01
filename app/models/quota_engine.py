from datetime import datetime, timedelta
from app.models.billing import BillingEvent


class QuotaEngine:

    def get_usage(self, db, user_id, period="day"):

        now = datetime.utcnow()

        if period == "day":
            start = now - timedelta(days=1)

        events = db.query(BillingEvent).filter(
            BillingEvent.user_id == user_id,
            BillingEvent.created_at >= start
        ).all()

        return {
            "requests": len(events),
            "tokens": sum(e.tokens_used for e in events),
            "cost": sum(e.cost_usd for e in events)
        }

    def check_limit(self, usage, plan):

        if usage["tokens"] > plan.max_tokens_per_day:
            return False, "TOKEN_LIMIT_EXCEEDED"

        if usage["requests"] > plan.max_requests_per_minute:
            return False, "RATE_LIMIT_EXCEEDED"

        return True, "OK"