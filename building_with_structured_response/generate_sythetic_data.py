import json
from typing import List

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field

from app import generate_chat


class QuestionAnswer(BaseModel):
    """
    Question & Answer Pairs from the text
    """

    question: str = Field(description="A question from the text")
    answer: str = Field(description="The answer to the question")
    source: str = Field(
        description=("The ground truth sentence from where the answer is " "derived")
    )


class Questions(BaseModel):
    """
    Generate questions & answers from the given text
    """

    questions: List[QuestionAnswer] = Field(
        description="A list of questions and answers from the text"
    )


def generate_qa_from_text(text: str) -> Questions:
    """Generate questions and answers from provided text."""
    prompt = (
        "Generate 5 questions and answers from the provided text. "
        "Return as JSON with this structure: "
        '{"questions": [{"question": "...", "answer": "...", '
        '"source": "..."}, ...]}\n\nText:\n'
        f"{text}"
    )

    response_text = generate_chat(prompt, response_format={"type": "json_object"})
    parsed_response = json.loads(response_text)

    return Questions(**parsed_response)


if __name__ == "__main__":
    response = requests.get("https://paulgraham.com/greatwork.html")
    soup = BeautifulSoup(response.text, "html.parser")

    body = soup.find("body")
    if body:
        text = body.get_text(separator=" ", strip=True)
    else:
        text = ""

    questions = generate_qa_from_text(text)
    print(questions.model_dump_json(indent=2))
