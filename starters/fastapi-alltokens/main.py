import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ALLTOKENS_API_KEY"),
    base_url=os.getenv("ALLTOKENS_BASE_URL"),
)

app = FastAPI(title="FastAPI + AllTokens")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    completion = client.chat.completions.create(
        model="router",
        messages=[{"role": "user", "content": req.message}],
    )

    return {
        "response": completion.choices[0].message.content
    }
