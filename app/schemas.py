from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class AssistantRequest(BaseModel):
    thread_id: Optional[str] = None
    message: str

class AssistantResponse(BaseModel):
    thread_id: str
    response: str
    status: str 