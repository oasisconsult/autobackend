import time


class RiskEngine:

    def calculate_risk(self, user, request, usage_stats):

        score = 0

        # 1. request frequency abuse
        if usage_stats["requests_last_minute"] > 20:
            score += 40

        # 2. token spike detection
        if usage_stats["avg_tokens"] > 5000:
            score += 20

        # 3. prompt length abuse (cost attack vector)
        if len(request.get("prompt", "")) > 8000:
            score += 25

        # 4. new account risk
        if usage_stats["account_age_days"] < 1:
            score += 15

        # 5. IP anomaly (basic heuristic)
        if user.get("ip_reputation") == "bad":
            score += 50

        return min(score, 100)