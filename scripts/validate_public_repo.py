#!/usr/bin/env python3
"""Public-safety and structure validator for this repository.

This is intentionally dependency-free so teams can run it before publishing
or wire it into GitHub Actions without extra setup.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATTERNS = {
    "openai_or_generic_secret_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "github_pat": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "github_classic_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private_key": re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "absolute_user_path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "database_url_value": re.compile(r"postgres(ql)?://[^\s]+:[^\s]+@"),
    "env_assignment_secret": re.compile(r"(?i)\b(password|secret|token|api_key|private_key)\s*=\s*['\"]?[^\s'\"]{8,}"),
    "linkedin_cookie": re.compile(r"\bli_at\b|\bJSESSIONID\b"),
}

REQUIRED_DOCS = [
    "README.md",
    "docs/operating-model.md",
    "docs/security-model.md",
    "docs/evals-and-benchmarks.md",
    "docs/failure-modes.md",
    "docs/prompt-blocks.md",
    "docs/case-study.md",
    "docs/recognition-plan.md",
    "docs/no-code-agent-ops.md",
]

REQUIRED_TEMPLATES = [
    "templates/agent-request.md",
    "templates/governed-task.md",
    "templates/security-review.md",
    "templates/pr-checklist.md",
]

REQUIRED_SCRIPTS = [
    "scripts/validate_public_repo.py",
    "scripts/agent_ops_init.py",
]

REQUIRED_AGENT_FIELDS = [
    "agent_id:",
    "version:",
    "description:",
    "reports_to:",
    "allowed_callers:",
    "allowed_callees:",
    "tools:",
    "memory_scope:",
    "write_scope:",
]

REQUIRED_AGENT_SECTIONS = [
    "# ",
    "## Role",
    "## Inputs",
    "## Outputs",
    "## Boundaries",
    "## Evals",
]

SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip"}:
            continue
        files.append(path)
    return files


def check_public_safety() -> list[str]:
    errors: list[str] = []
    for path in iter_text_files():
        text = path.read_text(errors="ignore")
        rel = path.relative_to(ROOT)
        for name, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{rel}: matched forbidden pattern {name}")
    return errors


def check_required_files(paths: list[str], label: str) -> list[str]:
    errors: list[str] = []
    for item in paths:
        if not (ROOT / item).exists():
            errors.append(f"missing {label}: {item}")
    return errors


def check_agent_directory(directory: Path, label: str, *, minimum_count: int = 1) -> list[str]:
    errors: list[str] = []
    agent_files = sorted(path for path in directory.glob("*.md") if path.name != "README.md")
    if not agent_files:
        return [f"missing {label} files"]
    if len(agent_files) < minimum_count:
        errors.append(f"{directory.relative_to(ROOT)}: expected at least {minimum_count} files")
    for path in agent_files:
        text = path.read_text(errors="ignore")
        rel = path.relative_to(ROOT)
        for field in REQUIRED_AGENT_FIELDS:
            if field not in text:
                errors.append(f"{rel}: missing field {field}")
        for section in REQUIRED_AGENT_SECTIONS:
            if section not in text:
                errors.append(f"{rel}: missing section {section}")
    return errors


def check_agent_examples() -> list[str]:
    return check_agent_directory(ROOT / "examples" / "agents", "agent example")


def check_software_team_agents() -> list[str]:
    return check_agent_directory(
        ROOT / "examples" / "software-team-agents",
        "software-team agent",
        minimum_count=8,
    )


def check_eval_examples() -> list[str]:
    errors: list[str] = []
    eval_files = sorted((ROOT / "examples" / "evals").glob("*.json"))
    if not eval_files:
        return ["missing eval example files"]
    for path in eval_files:
        text = path.read_text(errors="ignore")
        rel = path.relative_to(ROOT)
        if '"agent_id"' not in text:
            errors.append(f"{rel}: missing agent_id")
        if text.count('"prompt"') < 3:
            errors.append(f"{rel}: expected at least 3 prompts")
        if text.count('"expected_output"') < 3:
            errors.append(f"{rel}: expected at least 3 expected_output entries")
    return errors


def report(label: str, errors: list[str]) -> bool:
    if errors:
        print(f"FAIL {label}")
        for error in errors:
            print(f"  - {error}")
        return False
    print(f"PASS {label}")
    return True


def main() -> int:
    checks = [
        ("public safety scan", check_public_safety()),
        ("required docs", check_required_files(REQUIRED_DOCS, "doc")),
        ("templates", check_required_files(REQUIRED_TEMPLATES, "template")),
        ("scripts", check_required_files(REQUIRED_SCRIPTS, "script")),
        ("agent examples", check_agent_examples()),
        ("software-team agent pack", check_software_team_agents()),
        ("eval examples", check_eval_examples()),
    ]
    ok = True
    for label, errors in checks:
        ok = report(label, errors) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
