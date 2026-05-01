class CostCalculator:

    # rough production-safe estimates (adjust later)
    GPT_COST_PER_1K_TOKENS = 0.0005

    def calculate_llm_cost(self, tokens: int) -> float:
        return (tokens / 1000) * self.GPT_COST_PER_1K_TOKENS

    def calculate_generation_cost(self) -> float:
        return 0.05  # fixed cost per backend generation

    def calculate_total(self, tokens: int, generation_count: int = 1):
        return (
            self.calculate_llm_cost(tokens) +
            generation_count * self.calculate_generation_cost()
        )