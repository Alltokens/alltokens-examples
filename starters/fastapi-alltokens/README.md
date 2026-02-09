FastAPI + AllTokens starter

Minimal FastAPI backend using AllTokens as an OpenAI-compatible LLM gateway.

This starter shows:
- how to call AllTokens from backend code
- how to expose a simple HTTP API for chat completions

Requirements:
- Python 3.10+

Setup:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

Set ALLTOKENS_API_KEY in .env.

Run:

uvicorn main:app --reload --port 8000

Test:

curl http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
