from app.models.analytics_event import AnalyticsEvent


class EventCollector:

    def track(self, db, tenant_id, user_id, event_type, metadata=None):

        event = AnalyticsEvent(
            tenant_id=tenant_id,
            user_id=user_id,
            event_type=event_type,
            metadata=metadata or {}
        )

        db.add(event)
        db.commit()

        return event