"""Claude Agent SDK provider. Runs the local `claude` CLI, so it uses whatever auth the CLI has
(e.g. a Claude subscription after `claude login`, or ANTHROPIC_API_KEY)."""

import time
from pathlib import Path
from typing import Any, Callable, Optional

from gpt_resolve.providers.base import AgentResult, Provider
from gpt_resolve.providers.guard import check_tool_use

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
        on_event: Optional[Callable[[str], None]] = None,
        allowed_files: Optional[list[str]] = None,
    ) -> AgentResult:
        from claude_agent_sdk import (
            AssistantMessage,
            ClaudeAgentOptions,
            HookMatcher,
            ResultMessage,
            ToolUseBlock,
            query,
        )

        workdir.mkdir(parents=True, exist_ok=True)

        async def guard(input_data, tool_use_id, context):
            reason = check_tool_use(
                input_data["tool_name"], input_data["tool_input"], workdir, allowed_files or []
            )
            if reason is None:
                return {}
            if on_event:
                on_event(f"bloqueado: {reason}")
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }

        options = ClaudeAgentOptions(
            hooks={"PreToolUse": [HookMatcher(hooks=[guard])]} if allowed_files is not None else None,
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
            elif on_event and isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, ToolUseBlock):
                        on_event(describe_tool_use(block.name, block.input))

        if result is None:
            raise RuntimeError("Claude agent finished without a result message")
        if result.is_error:
            raise RuntimeError(
                f"Claude agent failed ({result.subtype}): {result.result or result.errors}"
            )
        if schema and result.structured_output is None:
            raise RuntimeError("Claude agent finished without the structured output")
        return AgentResult(
            text=result.result or "",
            structured=result.structured_output,
            cost_usd=result.total_cost_usd or 0.0,
            duration_s=time.perf_counter() - start,
            meta={"session_id": result.session_id, "num_turns": result.num_turns},
        )


def describe_tool_use(name: str, tool_input: dict[str, Any]) -> str:
    """One-line summary of a tool call for progress output."""
    if name == "Read":
        detail = Path(str(tool_input.get("file_path", ""))).name
        if tool_input.get("pages"):
            detail += f" (pág. {tool_input['pages']})"
    elif name == "Bash":
        detail = " ".join(str(tool_input.get("command", "")).split())[:90]
    elif name in ("Write", "Edit"):
        detail = Path(str(tool_input.get("file_path", ""))).name
    elif name == "StructuredOutput":
        return "entregando resultado"
    else:
        detail = str(tool_input)[:90]
    return f"{name}: {detail}"
