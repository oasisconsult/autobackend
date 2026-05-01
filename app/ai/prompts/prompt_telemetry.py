from collections import defaultdict


class PromptTelemetry:

    def __init__(self):
        self.data = defaultdict(lambda: {
            "runs": 0,
            "success": 0,
            "fail": 0,
            "scores": []
        })

    def log(self, prompt_name: str, success: bool, score: float):

        d = self.data[prompt_name]

        d["runs"] += 1
        d["success"] += int(success)
        d["fail"] += int(not success)
        d["scores"].append(score)

    def get_stats(self, prompt_name: str):

        d = self.data[prompt_name]

        avg_score = sum(d["scores"]) / len(d["scores"]) if d["scores"] else 0

        success_rate = d["success"] / d["runs"] if d["runs"] > 0 else 0

        return {
            "runs": d["runs"],
            "success_rate": success_rate,
            "avg_score": avg_score
        }