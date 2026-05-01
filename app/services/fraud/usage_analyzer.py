from app.models.billing import BillingEvent
from datetime import datetime, timedelta


class UsageAnalyzer:

    def get_stats(self, db, user_id):

        last_minute = datetime.utcnow() - timedelta(minutes=1)
        last_day = datetime.utcnow() - timedelta(days=1)

        events = db.query(BillingEvent).filter(
            BillingEvent.user_id == user_id
        ).all()

        requests_last_minute = len([
            e for e in events if e.created_at >= last_minute
        ])

        tokens = [e.tokens_used for e in events]

        avg_tokens = sum(tokens) / len(tokens) if tokens else 0

        return {
            "requests_last_minute": requests_last_minute,
            "avg_tokens": avg_tokens,
            "account_age_days": 1  # replace with real user model
        }