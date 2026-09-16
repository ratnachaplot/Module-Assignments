import anthropic
from ai_provider import AIProvider


class ClaudeProvider(AIProvider):

    def __init__(self):
        self.client = anthropic.Anthropic()

    def generate(self, prompt):
        response = self.client.messages.create(
            model="claude-3-5-haiku-latest",
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.content[0].text