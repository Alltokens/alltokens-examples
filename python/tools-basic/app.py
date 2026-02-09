from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]

resp = client.chat.completions.create(
    model="router",
    messages=[{"role": "user", "content": "Weather in Berlin?"}],
    tools=tools
)

print(resp)
