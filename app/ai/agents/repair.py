from app.ai.llm import call_llm


def run_repair(code: str, critique: str):
    """
    Fixes broken AI output
    """

    messages = [
        {
            "role": "system",
            "content": "Fix the backend code based on critique. Output full corrected version."
        },
        {
            "role": "user",
            "content": f"""
CODE:
{code}

ISSUES:
{critique}
"""
        }
    ]

    return call_llm(messages)