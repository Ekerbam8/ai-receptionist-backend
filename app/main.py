from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Allow frontend to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request body model
class MessageRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
async def chat_with_ai(request: MessageRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # ✅ Updated to new supported model
            messages=[
                {"role": "system", "content": "You are a helpful AI receptionist."},
                {"role": "user", "content": request.message},
            ]
        )
        reply = response.choices[0].message.content.strip()
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}

# Root endpoint for testing
@app.get("/")
async def root():
    return {"status": "AI Receptionist API running"}
