from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_ai(request: MessageRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI receptionist."},
                {"role": "user", "content": request.message},
            ]
        )
        reply = response.choices[0].message.content.strip()
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"status": "AI Receptionist API running"}
