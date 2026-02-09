from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

completion = client.chat.completions.create(
    model="router",
    messages=[{"role": "user", "content": "Summarize the benefits of multi-provider AI."}],
    extra_body={
        "metadata": {
            "objective": "cheapest",
            "max_cost_per_1k_tokens": 0.5
        }
    }
)

print(completion.choices[0].message.content)
