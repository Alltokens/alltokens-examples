from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

stream = client.chat.completions.create(
    model="router",
    messages=[{"role": "user", "content": "Explain routing in one paragraph."}],
    stream=True
)

for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
