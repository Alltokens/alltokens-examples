RAG + Qdrant + AllTokens

Minimal RAG example using:
- Qdrant vector database
- AllTokens embeddings and chat completions

Requirements:
- Docker
- Python 3.10+

Setup:

docker compose up -d
pip install -r requirements.txt
cp .env.example .env

Run:

python app.py
