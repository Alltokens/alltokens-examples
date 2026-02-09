from openai import OpenAI
import json

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

prompt = """
Extract name and company from this text:

"John works at Stripe"
Return JSON.
"""

completion = client.chat.completions.create(
    model="router",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"}
)

print(json.loads(completion.choices[0].message.content))
