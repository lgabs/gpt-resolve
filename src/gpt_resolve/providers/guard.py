"""Sandbox rules for exam agents: they may only read the exam files and use their own workdir,
with no network. Keeps answer keys or other files on the machine out of the agents' context."""

import re
from pathlib import Path
from typing import Any, Optional

# Prefixes a Bash command may reference besides the workdir and exam files (interpreters, LaTeX)
SYSTEM_PREFIXES = ("/usr/", "/bin/", "/opt/", "/Library/TeX/", "/dev/null")
NETWORK = re.compile(
    r"https?://|\b(curl|wget|nc|ncat|ssh|scp|rsync|ftp|telnet|pip|pip3|brew|apt|npm|git|open)\b"
    r"|\b(requests|urllib|httpx|socket|webbrowser)\b"
)
ESCAPES = re.compile(r"(^|[\s'\"=(])~|\$HOME|\$\{HOME\}|expanduser|\.\./|os\.environ")
# An absolute path starts a word (after whitespace, a quote, = ( < or >); this skips divisions like a/b
ABS_PATH = re.compile(r"(?:^|(?<=[\s'\"=(<>]))(/[^\s'\"`;|&()<>,]+)")


def _inside(path: str, roots: list[Path]) -> bool:
    try:
        resolved = Path(path).expanduser().resolve()
    except (OSError, RuntimeError):
        return False
    return any(resolved == r or r in resolved.parents for r in roots)


def check_tool_use(
    tool_name: str, tool_input: dict[str, Any], workdir: Path, allowed_files: list[str]
) -> Optional[str]:
    """Return a denial reason, or None when the tool call is allowed."""
    workdir = workdir.resolve()
    files = [Path(f).resolve() for f in allowed_files]
    roots = [workdir] + files

    if tool_name in ("Read", "Write", "Edit"):
        path = str(tool_input.get("file_path", ""))
        if not _inside(path if Path(path).is_absolute() else str(workdir / path), roots):
            return f"Acesso negado: use apenas os arquivos da prova ({', '.join(map(str, files))}) e a pasta de trabalho."
        return None

    if tool_name in ("Glob", "Grep"):
        path = str(tool_input.get("path") or workdir)
        if not _inside(path if Path(path).is_absolute() else str(workdir / path), [workdir]):
            return "Acesso negado: buscas só dentro da pasta de trabalho."
        return None

    if tool_name == "Bash":
        command = str(tool_input.get("command", ""))
        if NETWORK.search(command):
            return "Acesso negado: sem rede nem instalação de pacotes. Use python3 apenas para contas."
        if ESCAPES.search(command):
            return "Acesso negado: não acesse arquivos fora da pasta de trabalho."
        for path in ABS_PATH.findall(command):
            if not (path.startswith(SYSTEM_PREFIXES) or _inside(path, roots)):
                return f"Acesso negado a {path}: use apenas a pasta de trabalho e os arquivos da prova."
        return None

    if tool_name == "StructuredOutput":
        return None
    return f"Ferramenta {tool_name} não permitida."
