from fastapi import Request, HTTPException
from app.api.deps import get_current_user
from app.services.plan_resolver import PlanResolver
from app.services.quota_engine import QuotaEngine
from app.db.session import SessionLocal


class EnforcementMiddleware:

    def __init__(self):
        self.quota = QuotaEngine()
        self.plan_resolver = PlanResolver()

    async def __call__(self, request: Request, call_next):

        db = SessionLocal()

        try:
            user = get_current_user(
                request.headers.get("authorization")
            )

            tenant_id = user["tenant_id"]

            plan = self.plan_resolver.get_plan(db, tenant_id)

            if not plan:
                raise HTTPException(403, "No active plan")

            usage = self.quota.get_usage(db, user["sub"])

            allowed, reason = self.quota.check_limit(usage, plan)

            if not allowed:
                raise HTTPException(
                    status_code=429,
                    detail={
                        "error": reason,
                        "upgrade_required": True
                    }
                )

            response = await call_next(request)
            return response

        finally:
            db.close()