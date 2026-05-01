class UsageGrowthEngine:

    def evaluate_upgrade_trigger(self, usage: dict):

        if usage["generations"] > 5:
            return "SHOW_UPGRADE_MODAL"

        if usage["tokens"] > 5000:
            return "SUGGEST_PLAN_UPGRADE"

        return "NO_ACTION"