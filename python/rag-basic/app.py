from openai import OpenAI
import numpy as np

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

documents = [
    "AllTokens provides unified access to multiple LLM providers.",
    "Routing helps optimize cost and reliability.",
]

embeddings = [
    client.embeddings.create(
        model="text-embedding-3-large",
        input=doc
    ).data[0].embedding
    for doc in documents
]

query = "Why use routing?"

query_embedding = client.embeddings.create(
    model="text-embedding-3-large",
    input=query
).data[0].embedding


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


best_doc = documents[
    max(range(len(embeddings)),
        key=lambda i: cosine(query_embedding, embeddings[i]))
]

completion = client.chat.completions.create(
    model="router",
    messages=[
        {"role": "system", "content": f"Context: {best_doc}"},
        {"role": "user", "content": query},
    ],
)

print(completion.choices[0].message.content)
