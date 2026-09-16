from ollama_provider import OllamaProvider
from openai_provider import OpenAIProvider
from claude_provider import ClaudeProvider


def get_provider(provider_name):

    if provider_name == "ollama":
        return OllamaProvider()

    if provider_name == "openai":
        return OpenAIProvider()

    if provider_name == "claude":
        return ClaudeProvider()

    raise ValueError("Unknown provider")