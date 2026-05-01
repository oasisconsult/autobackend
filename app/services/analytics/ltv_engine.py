from app.models.analytics_event import AnalyticsEvent


class LTVEngine:

    def calculate_ltv(self, db, user_id):

        events = db.query(AnalyticsEvent).filter(
            AnalyticsEvent.user_id == user_id,
            AnalyticsEvent.event_type.in_(["payment_success", "upgrade"])
        ).all()

        total = sum(
            e.metadata.get("amount", 0) for e in events
        )

        return {
            "ltv": total
        }