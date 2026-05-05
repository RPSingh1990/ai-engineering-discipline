#!/usr/bin/env python3
"""Regression tests for Agent Ops contract enforcement."""

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


def run_validate(target: Path) -> subprocess.CompletedProcess[str]:
    return run_command(["python3", "scripts/agent_ops_validate.py", "--strict"], target)


def main() -> int:
    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "valid"
        init_demo(target)
        result = run_validate(target)
        assert result.returncode == 0, result.stdout + result.stderr

    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "blocked-tool"
        init_demo(target)
        backend = target / ".agent-ops" / "agents" / "backend-builder.md"
        backend.write_text(
            backend.read_text().replace(
                "tools: [repo_read, repo_write_backend, run_backend_tests]",
                "tools: [repo_read, direct_email_send]",
            )
        )
        result = run_validate(target)
        assert result.returncode != 0, "blocked tool should fail"
        assert "blocked tools" in result.stdout, result.stdout

    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "call-graph-drift"
        init_demo(target)
        product = target / ".agent-ops" / "agents" / "product-manager.md"
        product.write_text(
            product.read_text().replace(
                "allowed_callees: [orchestrator]",
                "allowed_callees: [orchestrator, backend-builder]",
            )
        )
        result = run_validate(target)
        assert result.returncode != 0, "call graph drift should fail"
        assert "call graph" in result.stdout, result.stdout

    print("PASS agent ops validate selftest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
