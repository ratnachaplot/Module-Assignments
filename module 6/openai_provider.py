from openai import OpenAI
from ai_provider import AIProvider


class OpenAIProvider(AIProvider):

    def __init__(self):
        self.client = OpenAI()

    def generate(self, prompt):
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text