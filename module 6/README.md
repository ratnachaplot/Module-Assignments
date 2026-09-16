# Module 6 - Provider-Agnostic AI Layer

## Objective

Build a common Python layer that can work with different AI providers without changing the main application code.

## Providers

- Ollama
- OpenAI
- Claude

## Architecture

main.py
   ↓
provider_factory.py
   ↓
AIProvider
   ↓
Ollama / OpenAI / Claude

## Common Interface

All providers implement:

generate(prompt)

This allows the application to use the same method regardless of which provider is selected.

## Provider Switching

The provider can be selected using:

get_provider("ollama")
get_provider("openai")
get_provider("claude")

Only the provider name needs to change in `main.py`.

## Testing

Ollama was tested successfully using the local Ollama server.

OpenAI integration was implemented, but live testing was not completed because the API account has no available credits.

Claude integration was implemented, but live API testing was not performed because API access/credits were not available.

## Conclusion

The provider-agnostic AI layer was successfully implemented. The application can use different AI providers through a common interface without changing the main application logic.