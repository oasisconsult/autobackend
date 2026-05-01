from app.ai.llm import call_llm


def run_architect(prompt: str):
    """
    Converts user idea → backend architecture
    """

    messages = [
        {
            "role": "system",
            "content": "You are a senior backend architect. Output ONLY FastAPI microservice architecture."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    return call_llm(messages)