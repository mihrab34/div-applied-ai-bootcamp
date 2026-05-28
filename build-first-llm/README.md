# LLM-101

================
# Overview

A project utilizing the Groq API to interact with various open source large language models (LLMs).

## Description
This project leverages the Groq API to generate responses to user queries using a selection of pre-trained LLMs. It includes a simple API that demonstrates the core functionality.

## Sample API response

<img width="975" height="738" alt="Screenshot 2025-09-03 at 11 40 34 PM" src="https://github.com/user-attachments/assets/4d83c931-5139-41f9-9b21-d49795c504c4" />

## Features
- Seamless integration with Groq API
- Support for multiple LLM models
- Easy-to-use script implementation

## Requirements
- groq
- uvicorn
- fastapi
- python-dotenv

## Usage
1. Install the required dependencies:
```bash
pip install -r requirements.txt
```
2. Set the `GROQ_API_KEY` environment variable using a `.env` file or your preferred method.
3. Run the server:
```bash
uvicorn app:app --reload
```
4. Open swagger UI: http://127.0.0.1:8000/docs

## Models
The project currently supports the following LLMs:
- qwen/qwen3-32b
- openai/gpt-oss-20b
- llama-3.3-70b-versatile
- gemma2-9b-it

## Generating Responses
The `generate_message` function takes in a model, query, and optional temperature parameter to generate a response. The response is then printed to the console.

## Contributing
