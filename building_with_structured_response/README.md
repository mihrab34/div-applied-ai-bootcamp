# Building with LLMs

Minimal FastAPI server with a health-check endpoint.

## Run the server

```bash
uv --cache-dir .uv-cache run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Health check

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{"status":"ok"}
```

FastAPI docs are available at:

```text
http://localhost:8000/docs
```

## Generate analysis

Add your Groq API key to `.env`:

```text
GROQ_API_KEY=your_api_key_here
```

Then call the analysis endpoint:

```bash
curl -X POST http://localhost:8000/analysis \
  -H "Content-Type: application/json" \
  -d '{"message":"Analyze sales by region and return a JSON object."}'
```

The default analysis temperature is `0.3`. The endpoint returns only validated JSON object responses.
