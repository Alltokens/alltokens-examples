import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

async def ask(q):
    resp = await client.chat.completions.create(
        model="router",
        messages=[{"role": "user", "content": q}]
    )
    print(resp.choices[0].message.content)

async def main():
    await asyncio.gather(
        ask("Explain routing"),
        ask("Explain vendor lock-in"),
        ask("Explain provider fallback"),
    )

asyncio.run(main())
