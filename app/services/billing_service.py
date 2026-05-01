from app.models.usage import Usage


class BillingService:

    def track_cost(self, db, user_id: str, tenant_id: str, cost: float):
        usage = Usage(
            user_id=user_id,
            tenant_id=tenant_id,
            cost=cost,
            tokens_used=int(cost * 100)
        )

        db.add(usage)
        db.commit()

        return usage


    def get_user_usage(self, db, user_id: str):
        return db.query(Usage).filter(
            Usage.user_id == user_id
        ).all()