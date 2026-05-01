from app.ai.prompts.prompt_telemetry import PromptTelemetry
from app.ai.prompts.prompt_scorer import PromptScorer
from app.ai.prompts.prompt_mutator import PromptMutator


class PromptOptimizer:

    def __init__(self):
        self.telemetry = PromptTelemetry()
        self.scorer = PromptScorer()
        self.mutator = PromptMutator()

    def process_result(self, prompt_name: str, prompt: str, output: dict):

        score = self.scorer.score(output)

        success = score > 70

        self.telemetry.log(prompt_name, success, score)

        stats = self.telemetry.get_stats(prompt_name)

        # 🔥 trigger learning only if system is unstable
        if stats["success_rate"] < 0.7 and stats["runs"] > 5:

            improved_prompt = self.mutator.mutate(
                prompt,
                {
                    "stats": stats,
                    "last_output": output
                }
            )

            return {
                "updated_prompt": improved_prompt,
                "stats": stats
            }

        return {
            "stats": stats
        }