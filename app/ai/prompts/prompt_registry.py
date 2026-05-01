import uuid
from datetime import datetime


class PromptRegistry:

    def __init__(self):
        self.prompts = {}

    def register(self, name: str, template: str):

        self.prompts[name] = {
            "id": str(uuid.uuid4()),
            "template": template,
            "version": 1,
            "success_rate": 0.0,
            "avg_score": 0.0,
            "created_at": datetime.utcnow()
        }

    def get(self, name: str):
        return self.prompts.get(name)