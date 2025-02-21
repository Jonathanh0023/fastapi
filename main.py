from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import AssistantRequest, AssistantResponse
from app.services.assistant_service import AssistantService

app = FastAPI(title="OpenAI Assistant API")

# CORS-Middleware-Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sw01.rogsurvey.de"],  # Erlaubte Ursprünge
    allow_credentials=True,
    allow_methods=["*"],  # Erlaubte HTTP-Methoden
    allow_headers=["*"],  # Erlaubte HTTP-Header
)

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