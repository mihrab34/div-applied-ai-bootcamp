import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


from app import generate_chat


class AnalysisRequest(BaseModel):
    message: str
    temperature: float = 0.3


class AnalysisResponse(BaseModel):
    summary: str
    sentiment: str
    tags: list[str]


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
