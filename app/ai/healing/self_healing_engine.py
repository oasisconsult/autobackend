from app.ai.healing.failure_classifier import FailureClassifier
from app.ai.healing.diagnoser import Diagnoser
from app.ai.healing.repair_engine import RepairEngine


class SelfHealingEngine:

    def __init__(self):
        self.classifier = FailureClassifier()
        self.diagnoser = Diagnoser()
        self.repair = RepairEngine()

    def run(self, prompt: str, generator_fn, max_attempts=2):

        attempt = 0
        output = None
        error = None

        while attempt < max_attempts:

            try:
                output = generator_fn(prompt)

                if output and len(output) > 50:
                    return {
                        "status": "success",
                        "output": output,
                        "attempts": attempt + 1
                    }

            except Exception as e:
                error = str(e)

            # 1. classify failure
            failure_type = self.classifier.classify(error, output)

            # 2. diagnose
            diagnosis = self.diagnoser.analyze(
                failure_type,
                {"prompt": prompt, "output": output}
            )

            # 3. repair strategy
            prompt = self.repair.fix_prompt(prompt, diagnosis)

            attempt += 1

        return {
            "status": "failed",
            "last_error": error,
            "attempts": attempt
        }