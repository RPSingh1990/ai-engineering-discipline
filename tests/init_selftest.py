#!/usr/bin/env python3
"""Regression test for the Agent Ops initializer."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = [
    ".agent-ops/README.md",
    ".agent-ops/templates/agent-request.md",
    ".agent-ops/templates/governed-task.md",
    ".agent-ops/templates/security-review.md",
    ".agent-ops/registry/call-graph.yaml",
    ".agent-ops/registry/tool-acl.yaml",
    ".agent-ops/registry/governed-channels.yaml",
    ".agent-ops/agents/orchestrator.md",
    ".agent-ops/agents/product-manager.md",
    ".agent-ops/agents/architecture.md",
    ".agent-ops/agents/backend-builder.md",
    ".agent-ops/agents/frontend-builder.md",
    ".agent-ops/agents/data-engineer.md",
    ".agent-ops/agents/security-reviewer.md",
    ".agent-ops/agents/qa-reviewer.md",
    ".agent-ops/agents/code-reviewer.md",
    ".agent-ops/agents/research-analyst.md",
    ".agent-ops/agents/devops-release.md",
    ".agent-ops/tasks/password-reset-trust-gate.md",
    ".agent-ops/reviews/password-reset-sample-review.md",
    ".agent-ops/evals/backend-builder-evals.json",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/agent-ops-validate.yml",
    "scripts/agent_ops_validate.py",
    "scripts/agent_ops_guard.py",
]


def main() -> int:
    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "product-repo"
        result = subprocess.run(
            [
                "python3",
                str(ROOT / "scripts" / "agent_ops_init.py"),
                "--target",
                str(target),
                "--demo",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            return result.returncode

        missing = [item for item in EXPECTED_FILES if not (target / item).is_file()]
        if missing:
            print("FAIL missing initialized files")
            for item in missing:
                print(f"  - {item}")
            return 1

        validate = subprocess.run(
            ["python3", str(target / "scripts" / "agent_ops_validate.py"), "--strict"],
            cwd=target,
            check=False,
            capture_output=True,
            text=True,
        )
        if validate.returncode != 0:
            print(validate.stdout)
            print(validate.stderr)
            return validate.returncode

    print("PASS agent ops init selftest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
