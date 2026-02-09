RAG + Postgres (pgvector) + AllTokens

Minimal Retrieval-Augmented Generation example using:
- PostgreSQL
- pgvector
- AllTokens for embeddings and chat completions

This is intentionally simple and educational.

Requirements:
- Docker
- Python 3.10+

Setup:

docker compose up -d
pip install -r requirements.txt
cp .env.example .env

Run:

python app.py
