class PromptScorer:

    def score(self, output: dict):

        score = 0

        if output.get("status") == "success":
            score += 50

        if output.get("runtime_valid"):
            score += 30

        if output.get("critique") and "MAJOR" not in output["critique"]:
            score += 10

        if output.get("attempts", 1) <= 2:
            score += 10

        return min(score, 100)