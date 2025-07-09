# AI Receptionist Backend

A FastAPI backend that connects to OpenAI GPT-4 to respond to user questions like a receptionist.

## Usage

Send a POST request to `/chat` with a JSON body:
```json
{ "message": "Hello" }
