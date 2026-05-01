class DecisionEngine:

    def evaluate(self, risk_score: int):

        if risk_score < 30:
            return "ALLOW"

        if risk_score < 60:
            return "THROTTLE"

        if risk_score < 80:
            return "CHALLENGE"

        return "BLOCK"