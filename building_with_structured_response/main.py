import json

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import generate_chat
from generate_sythetic_data import generate_qa_from_text


class AnalysisRequest(BaseModel):
    message: str
    temperature: float = 0.3


class AnalysisResponse(BaseModel):
    summary: str
    sentiment: str
    tags: list[str]


class GenerateDataRequest(BaseModel):
    prompt: str
    temperature: float = 0.3


class GenerateDataResponse(BaseModel):
    data: dict


app = FastAPI(title="Building with LLMs API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Building with LLMs API is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analysis", response_model=AnalysisResponse)
def analysis(request: AnalysisRequest) -> AnalysisResponse:
    try:
        response = generate_chat(
            request.message,
            temperature=request.temperature,
        )
        parsed_response = json.loads(response)

        if not isinstance(parsed_response, dict):
            raise ValueError("Analysis response must be a JSON object")

        return AnalysisResponse(**parsed_response)
    except json.JSONDecodeError as exc:
        raise HTTPException(
            status_code=502,
            detail="Analysis response was not valid JSON",
        ) from exc
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate analysis",
        ) from exc


@app.post("/generate_data", response_model=GenerateDataResponse)
def data_generation(request: GenerateDataRequest) -> GenerateDataResponse:
    try:
        # Crawl the Paul Graham webpage
        response = requests.get("https://paulgraham.com/greatwork.html")
        soup = BeautifulSoup(response.text, "html.parser")

        body = soup.find("body")
        if body:
            text = body.get_text(separator=" ", strip=True)
        else:
            text = ""

        # Generate Q&A from the crawled text
        questions = generate_qa_from_text(text)
        return GenerateDataResponse(data=questions.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate data",
        ) from exc
