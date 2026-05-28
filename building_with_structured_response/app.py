import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

DEFAULT_SYSTEM_PROMPT = """You are a data analysis assistant. Your task is to analyze the provided text and return a JSON object with these exact fields:
{
  "summary": "A brief 1-2 sentence summary of the key points",
  "sentiment": "One of: positive, negative, or neutral",
  "tags": ["tag1", "tag2", "tag3"]
}

IMPORTANT: Return ONLY valid JSON, no other text or explanation."""

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

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
    response_format: dict | None = None,
) -> str:
    client = get_groq_client()
    kwargs = {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "model": model,
        "temperature": temperature,
    }

    if response_format:
        kwargs["response_format"] = response_format

    chat_completion = client.chat.completions.create(**kwargs)

    return chat_completion.choices[0].message.content or ""


def main():
    print("Hello from building-with-llms!")


if __name__ == "__main__":
    main()
