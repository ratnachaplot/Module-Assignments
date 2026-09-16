from provider_factory import get_provider


ai = get_provider("ollama")

response = ai.generate("What is Python?")

print(response)