"""Provider interface: anything that can run an agent task and return text or structured output."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional


@dataclass
class AgentResult:
    text: str
    structured: Optional[dict[str, Any]] = None
    cost_usd: float = 0.0
    duration_s: float = 0.0
    meta: dict[str, Any] = field(default_factory=dict)


class Provider(ABC):
    """An agent backend. Each `run` call is an isolated agent session (a "subagent")."""

    name: str = "base"

    @abstractmethod
    async def run(
        self,
        *,
        prompt: str,
        system_prompt: str,
        model: str,
        workdir: Path,
        schema: Optional[dict[str, Any]] = None,
        effort: Optional[str] = None,
        max_turns: Optional[int] = None,
        on_event: Optional[Callable[[str], None]] = None,
        allowed_files: Optional[list[str]] = None,
    ) -> AgentResult:
        """Run one agent task. `on_event` receives short progress lines (e.g. tool calls).
        When `allowed_files` is given, the agent may only read those files and its workdir, with no network. When `schema` is given, `AgentResult.structured` must follow it."""
