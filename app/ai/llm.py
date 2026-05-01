from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def call_llm(messages, model="gpt-5-mini", temperature=0.2):
    """
    Central LLM wrapper:
    - controls cost
    - standardises calls
    - future-proofs model swaps
    """

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content