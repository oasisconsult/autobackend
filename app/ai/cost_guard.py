from app.core.config import settings


class CostGuard:

    def __init__(self):
        self.max_cost = settings.MAX_AI_COST_PER_REQUEST

    def estimate_cost(self, tokens: int) -> float:
        return tokens * 0.00002  # rough GPT estimate

    def validate(self, estimated_cost: float):
        if estimated_cost > self.max_cost:
            raise Exception("Cost limit exceeded")

    def check_tokens(self, prompt: str):
        tokens = len(prompt.split())
        cost = self.estimate_cost(tokens)
        self.validate(cost)