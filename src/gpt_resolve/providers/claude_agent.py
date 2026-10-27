"""Claude Agent SDK provider. Runs the local `claude` CLI, so it uses whatever auth the CLI has
(e.g. a Claude subscription after `claude login`, or ANTHROPIC_API_KEY)."""

import time
from pathlib import Path
from typing import Any, Optional

from gpt_resolve.providers.base import AgentResult, Provider

# Tools the agents may use: read the exam (PDF pages / images) and run Python/LaTeX to check work.
AGENT_TOOLS = ["Read", "Glob", "Grep", "Bash", "Write"]


class ClaudeAgentProvider(Provider):
    name = "claude"

    def __init__(self, cli_path: Optional[str] = None):
        self.cli_path = cli_path

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
    ) -> AgentResult:
        from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

        workdir.mkdir(parents=True, exist_ok=True)
        options = ClaudeAgentOptions(
            model=model,
            system_prompt=system_prompt,
            cwd=str(workdir),
            tools=AGENT_TOOLS,
            allowed_tools=AGENT_TOOLS,
            # Agents work in a scratch dir on local exam files; no prompts mid-run.
            permission_mode="bypassPermissions",
            setting_sources=[],
            max_turns=max_turns,
            effort=effort,
            output_format={"type": "json_schema", "schema": schema} if schema else None,
            cli_path=self.cli_path,
        )

        start = time.perf_counter()
        result: Optional[ResultMessage] = None
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, ResultMessage):
                result = message

        if result is None:
            raise RuntimeError("Claude agent finished without a result message")
        if result.is_error:
            raise RuntimeError(
                f"Claude agent failed ({result.subtype}): {result.result or result.errors}"
            )
        return AgentResult(
            text=result.result or "",
            structured=result.structured_output,
            cost_usd=result.total_cost_usd or 0.0,
            duration_s=time.perf_counter() - start,
            meta={"session_id": result.session_id, "num_turns": result.num_turns},
        )
