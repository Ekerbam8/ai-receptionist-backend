from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

# Set up client with your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
