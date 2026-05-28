# DIV Applied AI Bootcamp

A collection of LLM-powered applications built during the DIV Applied AI Bootcamp. These projects demonstrate practical implementations of AI/LLM integrations using FastAPI and the Groq API.

## About This Repository

This repository contains hands-on projects for learning how to build AI-powered applications:

- **build-first-llm**: A foundational FastAPI application that integrates with the Groq LLM API to provide chat capabilities and health checks.
- **building_with_structured_response**: An advanced LLM application that focuses on generating structured JSON and Markdown responses for data analysis tasks.

Both projects use the Groq API for fast, efficient LLM inference.

## Prerequisites

Before getting started, ensure you have:

- **Python 3.13+** installed on your system
- **Groq API key** (sign up at <https://console.groq.com/>)
- **uv** package manager (install from <https://docs.astral.sh/uv/>) or **pip**

## Getting Started

### 1. Clone or Navigate to the Repository

```bash
cd /Users/rahmatbilesanmi/Documents/DIV_Bootcamp
```

### 2. Set Up Your Environment Variables

Create a `.env` file in the project directory with your Groq API credentials:

```
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### 3. Choose a Project and Install Dependencies

#### For build-first-llm

```bash
cd build-first-llm
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

#### For building_with_structured_response

```bash
cd building_with_structured_response
uv sync
```

This will automatically create a virtual environment and install dependencies from the `uv.lock` file.

### 4. Run the Application

```bash
python app.py
```

The FastAPI server will start at `http://localhost:8000`

## API Endpoints

### Health Check

```md
GET /healthstatus
```

### Chat Endpoint

```md
POST /chat
Content-Type: application/json

{
"model": "groq",
"question": "Your question here",
"temperature": 0.7
}
```

## Project Structure

```
DIV_Bootcamp/
├── build-first-llm/           # Basic LLM chat API
│   ├── app.py                 # FastAPI application
│   ├── main.py                # Core LLM logic
│   ├── requirements.txt        # Dependencies
│   └── env/                   # Virtual environment
│
└── building_with_structured_response/  # Advanced structured responses
    ├── app.py                 # FastAPI application
    ├── pyproject.toml         # Project configuration
    └── .venv/                 # Virtual environment
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Groq**: Python client for Groq LLM API
- **python-dotenv**: Environment variable management

## Troubleshooting

- **API Key Error**: Ensure your `GROQ_API_KEY` is set in the `.env` file
- **Module Not Found**: Make sure you've activated the virtual environment and installed dependencies
- **Port Already in Use**: The server runs on port 8000 by default. Modify `uvicorn.run()` if needed

## Resources

- [Groq Documentation](https://console.groq.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
