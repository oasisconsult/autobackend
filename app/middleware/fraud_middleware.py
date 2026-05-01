from fastapi import Request, HTTPException
from app.services.fraud.risk_engine import RiskEngine
from app.services.fraud.behavior_tracker import BehaviorTracker
from app.services.fraud.usage_analyzer import UsageAnalyzer
from app.services.fraud.decision_engine import DecisionEngine
from app.db.session import SessionLocal
from app.api.deps import get_current_user


class FraudMiddleware:

    def __init__(self):
        self.risk = RiskEngine()
        self.tracker = BehaviorTracker()
        self.analyzer = UsageAnalyzer()
        self.decision = DecisionEngine()

    async def __call__(self, request: Request, call_next):

        db = SessionLocal()

        try:
            user = get_current_user(
                request.headers.get("authorization")
            )

            user_id = user["sub"]

            # 1. record behavior
            self.tracker.record_request(user_id)

            # 2. analyze usage
            stats = self.analyzer.get_stats(db, user_id)

            # 3. calculate risk
            risk_score = self.risk.calculate_risk(
                user,
                await request.json() if request.method == "POST" else {},
                stats
            )

            # 4. decide action
            decision = self.decision.evaluate(risk_score)

            if decision == "BLOCK":
                raise HTTPException(403, "Request blocked due to abuse detection")

            if decision == "CHALLENGE":
                return HTTPException(
                    429,
                    "Suspicious activity detected. Please slow down."
                )

            if decision == "THROTTLE":
                request.state.throttle = True

            return await call_next(request)

        finally:
            db.close()