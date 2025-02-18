from openai import OpenAI
from app.config import settings
import time

class AssistantService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        # Ersetzen Sie diese ID mit Ihrer eigenen Assistant-ID
        self.assistant_id = "asst_0WspY2xisQIJF5htNi6HueDV"

    async def process_message(self, message: str, thread_id: str = None) -> dict:
        # Thread erstellen oder vorhandenen verwenden
        if thread_id is None:
            thread = self.client.beta.threads.create()
            thread_id = thread.id
        
        # Nachricht zum Thread hinzufügen
        message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=message
        )

        # Run erstellen und ausführen
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=self.assistant_id
        )

        # Auf Fertigstellung warten
        while True:
            run_status = self.client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
            if run_status.status == 'completed':
                break
            time.sleep(1)

        # Antwort abrufen
        messages = self.client.beta.threads.messages.list(thread_id=thread_id)
        assistant_message = next(msg for msg in messages if msg.role == "assistant")
        
        return {
            "thread_id": thread_id,
            "response": assistant_message.content[0].text.value,
            "status": "success"
        } 