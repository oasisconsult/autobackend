from app.ai.llm import call_llm


class Diagnoser:

    def analyze(self, failure_type: str, context: dict):

        prompt = f"""
You are a senior AI system debugger.

Failure type: {failure_type}

Context:
{context}

Identify the root cause and suggest a fix strategy:
- prompt_fix
- architecture_fix
- retry
- model_switch
- ignore (non-critical)
"""

        return call_llm([
            {"role": "user", "content": prompt}
        ])