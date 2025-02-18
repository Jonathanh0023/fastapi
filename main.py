from fastapi import FastAPI, HTTPException
from app.schemas import AssistantRequest, AssistantResponse
from app.services.assistant_service import AssistantService

app = FastAPI(title="OpenAI Assistant API")
assistant_service = AssistantService()

@app.post("/chat", response_model=AssistantResponse)
async def chat_with_assistant(request: AssistantRequest):
    try:
        response = await assistant_service.process_message(
            message=request.message,
            thread_id=request.thread_id
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "OpenAI Assistant API is running"
    }