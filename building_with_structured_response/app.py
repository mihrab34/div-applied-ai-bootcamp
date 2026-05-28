import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

DEFAULT_SYSTEM_PROMPT = """You are a data analysis assistant. \
    Your goal is to provide accurate, useful, and relevant \
        analysis for my request. Return only valid JSON or Markdown output."""

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

_groq_client: Groq | None = None


def get_groq_client() -> Groq:
    global _groq_client

    if _groq_client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY is not set")
        _groq_client = Groq(api_key=api_key)

    return _groq_client


def generate_chat(
    user_prompt: str,
    temperature: float = 0.3,
    model: str = DEFAULT_MODEL,
) -> str:
    client = get_groq_client()
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        model=model,
        temperature=temperature,
    )

    return chat_completion.choices[0].message.content or ""


def main():
    print("Hello from building-with-llms!")


if __name__ == "__main__":
    main()
