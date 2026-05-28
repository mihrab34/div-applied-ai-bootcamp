import os
import random

import groq
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


# set GROQ API KEY from env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)


sys_prompt = """You are a helpful virtual assistant. \
    Your goal is to provide useful and relevant \
        responses to my request"""

models = [
    "qwen/qwen3-32b",
    "openai/gpt-oss-20b",
    "llama-3.3-70b-versatile",
    "gemma2-9b-it",
]


def generate_message(model, query, temperature=0.0):
    try:
        response = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": query},
            ],
            model=model,
            temperature=temperature,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    model = random.choice(models)
    query = "What is the capital of France?"
    response = generate_message(model, query)
    print(response)
