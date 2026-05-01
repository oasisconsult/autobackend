class RevenueEngine:

    def calculate_ltv(self, usage, subscription):

        base = subscription["price"]

        usage_multiplier = usage["generations"] * 0.5

        return base + usage_multiplier

    def detect_churn_risk(self, usage):

        if usage["last_active_days"] > 3:
            return "HIGH_RISK"

        return "LOW_RISK"