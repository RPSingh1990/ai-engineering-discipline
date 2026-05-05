#!/usr/bin/env python3
"""Regression tests for the runtime Agent Ops guard."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, check=False, capture_output=True, text=True)


def init_demo(target: Path) -> None:
    result = run_command(
        [
            "python3",
            str(ROOT / "scripts" / "agent_ops_init.py"),
            "--target",
            str(target),
            "--demo",
        ],
        ROOT,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def main() -> int:
    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "guarded"
        init_demo(target)

        allow_tool = run_command(["python3", "scripts/agent_ops_guard.py", "tool", "backend-builder", "repo_read"], target)
        assert allow_tool.returncode == 0, allow_tool.stdout + allow_tool.stderr

        deny_tool = run_command(["python3", "scripts/agent_ops_guard.py", "tool", "backend-builder", "direct_email_send"], target)
        assert deny_tool.returncode != 0, "blocked tool should be denied"
        assert "DENY" in deny_tool.stdout, deny_tool.stdout

        deny_call = run_command(["python3", "scripts/agent_ops_guard.py", "call", "product-manager", "backend-builder"], target)
        assert deny_call.returncode != 0, "blocked call should be denied"

        evidence = (
            '{"approval_id":"A1","approved_by":"owner","approved_at":"now",'
            '"recipient":"user@example.com","evidence_ref":"log-1",'
            '"audit_log":"audit-1","failure_path":"retry"}'
        )
        allow_channel = run_command(
            ["python3", "scripts/agent_ops_guard.py", "channel", "email_send", "--evidence", evidence],
            target,
        )
        assert allow_channel.returncode == 0, allow_channel.stdout + allow_channel.stderr

    print("PASS agent ops guard selftest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
