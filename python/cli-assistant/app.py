from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

while True:
    question = input(">>> ")

    resp = client.chat.completions.create(
        model="router",
        messages=[{"role": "user", "content": question}]
    )

    print(resp.choices[0].message.content)
