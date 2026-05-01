from app.models.plan import Plan
from app.models.tenant_subscription import TenantSubscription


class PlanResolver:

    def get_plan(self, db, tenant_id):

        sub = db.query(TenantSubscription).filter(
            TenantSubscription.tenant_id == tenant_id
        ).first()

        if not sub:
            return None

        return db.query(Plan).filter(
            Plan.id == sub.plan_id
        ).first()