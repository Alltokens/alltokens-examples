import os
import psycopg2
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ALLTOKENS_API_KEY"),
    base_url=os.getenv("ALLTOKENS_BASE_URL"),
)

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS docs (
  id SERIAL PRIMARY KEY,
  content TEXT,
  embedding VECTOR(3072)
);
""")
conn.commit()

docs = [
    "AllTokens provides a unified OpenAI-compatible API.",
    "Routing allows cost and reliability optimization."
]

for doc in docs:
    emb = client.embeddings.create(
        model="text-embedding-3-large",
        input=doc
    ).data[0].embedding

    cur.execute(
        "INSERT INTO docs (content, embedding) VALUES (%s, %s)",
        (doc, emb)
    )
conn.commit()

query = "Why is routing useful?"

query_emb = client.embeddings.create(
    model="text-embedding-3-large",
    input=query
).data[0].embedding

cur.execute("""
SELECT content
FROM docs
ORDER BY embedding <-> %s
LIMIT 1
""", (query_emb,))

context = cur.fetchone()[0]

completion = client.chat.completions.create(
    model="router",
    messages=[
        {"role": "system", "content": f"Context: {context}"},
        {"role": "user", "content": query}
    ]
)

print(completion.choices[0].message.content)
