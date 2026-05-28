import traceback

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from main import generate_message, models

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello LLM API"}


@app.get("/healthstatus")
async def check_health_status():
    return {"application": "Simple LLM API", "message": "running succesfully"}


@app.post("/chat")
async def generate_chat(request: Request):

    query = await request.json()
    model = query["model"]

    try:
        temperature = float(query["temperature"])
    except (KeyError, ValueError):
        return {"error": "Invalid input, pass a number between 0 and 2."}

    if model not in models:
        return {"error": "You did not pass a correct model code!"}

    try:
        response = generate_message(model, query["question"], temperature=temperature)

        return {"status": "success", "response": response}

    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e), "status_code": 400}


if __name__ == "__main__":
    import uvicorn

    print("Starting LLM API")
    uvicorn.run(app, host="0.0.0.0", reload=True)
