from gpt_resolve.providers.base import AgentResult, Provider


def get_provider(name: str) -> Provider:
    """Build a provider by name. Add new backends here."""
    if name == "claude":
        from gpt_resolve.providers.claude_agent import ClaudeAgentProvider

        return ClaudeAgentProvider()
    if name == "mock":
        from gpt_resolve.providers.mock import MockProvider

        return MockProvider()
    raise ValueError(f"Unknown provider '{name}'. Available: claude, mock")


__all__ = ["AgentResult", "Provider", "get_provider"]
