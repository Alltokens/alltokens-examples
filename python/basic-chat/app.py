from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

completion = client.chat.completions.create(
    model="router",
    messages=[
        {"role": "user", "content": "Write a haiku about infrastructure."}
    ],
)

print(completion.choices[0].message.content)
