from openai import OpenAI

client = OpenAI()

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
