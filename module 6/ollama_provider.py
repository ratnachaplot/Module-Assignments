import requests
from ai_provider import AIProvider


class OllamaProvider(AIProvider):

    def generate(self, prompt):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return result["response"]