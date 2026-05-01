from app.ai.llm import call_llm


class PromptMutator:

    def mutate(self, prompt: str, failure_data: dict):

        response = call_llm([
            {
                "role": "system",
                "content": """
You are a prompt optimisation engine.
Your job is to improve prompts based on failure patterns.

Rules:
- Keep intent unchanged
- Improve clarity and success rate
- Remove ambiguity
- Make instructions more structured
Return ONLY the improved prompt.
"""
            },
            {
                "role": "user",
                "content": f"""
Original Prompt:
{prompt}

Failure Data:
{failure_data}
"""
            }
        ])

        return response