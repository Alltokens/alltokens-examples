import os
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ALLTOKENS_API_KEY"),
    base_url=os.getenv("ALLTOKENS_BASE_URL"),
)

qdrant = QdrantClient(host="localhost", port=6333)

qdrant.recreate_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
)

docs = [
    "AllTokens is a unified LLM gateway.",
    "Routing enables vendor-neutral AI systems."
]

points = []

for i, doc in enumerate(docs):
    emb = client.embeddings.create(
        model="text-embedding-3-large",
        input=doc
    ).data[0].embedding

    points.append(
        PointStruct(id=i, vector=emb, payload={"text": doc})
    )

qdrant.upsert(collection_name="docs", points=points)

query = "Why use a gateway?"

query_emb = client.embeddings.create(
    model="text-embedding-3-large",
    input=query
).data[0].embedding

hits = qdrant.search(
    collection_name="docs",
    query_vector=query_emb,
    limit=1,
)

context = hits[0].payload["text"]

completion = client.chat.completions.create(
    model="router",
    messages=[
        {"role": "system", "content": f"Context: {context}"},
        {"role": "user", "content": query}
    ]
)

print(completion.choices[0].message.content)
