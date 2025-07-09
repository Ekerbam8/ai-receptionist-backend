from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_ai(request: MessageRequest):
    try:
        response = openai.ChatCompletion.create(
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
def root():
    return {"status": "API running"}
