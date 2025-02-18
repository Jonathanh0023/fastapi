from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")

settings = Settings()

# Überprüfung des API-Keys
if not settings.openai_api_key:
    raise ValueError("OPENAI_API_KEY muss in den Umgebungsvariablen gesetzt sein") 