from sqlalchemy.orm import Session
from app.models.usage import Usage


class MemoryStore:

    def log_event(self, db: Session, user_id: str, event: str):
        """
        Lightweight behavioural memory for:
        - improving prompts
        - tracking failure patterns
        """

        record = Usage(
            user_id=user_id,
            tenant_id=None,
            tokens_used=0,
            cost=0
        )

        db.add(record)
        db.commit()