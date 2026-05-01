from app.models.usage import Usage


class UsageService:

    def get_total_usage(self, db, user_id: str) -> int:
        usage = db.query(Usage).filter(
            Usage.user_id == user_id
        ).all()

        return sum(u.tokens_used for u in usage)


    def can_run_generation(self, db, user_id: str, limit: int = 1000) -> bool:
        total = self.get_total_usage(db, user_id)
        return total < limit