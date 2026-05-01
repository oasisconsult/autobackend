from app.ai.llm import call_llm


def run_critic(code: str):
    """
    Detects:
    - missing components
    - broken architecture
    - unsafe patterns
    """

    messages = [
        {
            "role": "system",
            "content": "You are a strict code reviewer. Identify ALL issues. Return PASS or FAIL with reasons."
        },
        {
            "role": "user",
            "content": code
        }
    ]

    return call_llm(messages)