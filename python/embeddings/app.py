from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

embedding = client.embeddings.create(
    model="text-embedding-3-large",
    input="AllTokens enables vendor-neutral AI infrastructure."
)

print(len(embedding.data[0].embedding))
