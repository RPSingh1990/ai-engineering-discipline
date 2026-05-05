#!/usr/bin/env python3
"""Initialize a lightweight Agent Ops scaffold in another repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES_TO_COPY = [
    ("templates/agent-request.md", ".agent-ops/templates/agent-request.md"),
    ("templates/governed-task.md", ".agent-ops/templates/governed-task.md"),
    ("templates/security-review.md", ".agent-ops/templates/security-review.md"),
    ("templates/pr-checklist.md", ".github/PULL_REQUEST_TEMPLATE.md"),
    ("templates/agent-ops-validate.yml", ".github/workflows/agent-ops-validate.yml"),
    ("scripts/agent_ops_validate.py", "scripts/agent_ops_validate.py"),
    ("scripts/agent_ops_guard.py", "scripts/agent_ops_guard.py"),
    ("scripts/run_evals.py", "scripts/run_evals.py"),
    ("examples/registry/call-graph.example.yaml", ".agent-ops/registry/call-graph.yaml"),
    ("examples/registry/tool-acl.example.yaml", ".agent-ops/registry/tool-acl.yaml"),
    ("examples/registry/governed-channels.example.yaml", ".agent-ops/registry/governed-channels.yaml"),
    ("examples/software-team-agents/orchestrator.md", ".agent-ops/agents/orchestrator.md"),
    ("examples/software-team-agents/product-manager.md", ".agent-ops/agents/product-manager.md"),
    ("examples/software-team-agents/architecture.md", ".agent-ops/agents/architecture.md"),
    ("examples/software-team-agents/backend-builder.md", ".agent-ops/agents/backend-builder.md"),
    ("examples/software-team-agents/frontend-builder.md", ".agent-ops/agents/frontend-builder.md"),
    ("examples/software-team-agents/data-engineer.md", ".agent-ops/agents/data-engineer.md"),
    ("examples/software-team-agents/security-reviewer.md", ".agent-ops/agents/security-reviewer.md"),
    ("examples/software-team-agents/qa-reviewer.md", ".agent-ops/agents/qa-reviewer.md"),
    ("examples/software-team-agents/code-reviewer.md", ".agent-ops/agents/code-reviewer.md"),
    ("examples/software-team-agents/research-analyst.md", ".agent-ops/agents/research-analyst.md"),
    ("examples/software-team-agents/devops-release.md", ".agent-ops/agents/devops-release.md"),
]

DEMO_FILES = [
    ("examples/worked-example/governed-task.md", ".agent-ops/tasks/password-reset-trust-gate.md"),
    ("examples/worked-example/sample-review.md", ".agent-ops/reviews/password-reset-sample-review.md"),
    ("examples/evals/agent-contract-evals.json", ".agent-ops/evals/agent-contract-evals.json"),
    ("examples/evals/outputs/auth-password-reset-provider-failure.md", ".agent-ops/evals/outputs/auth-password-reset-provider-failure.md"),
    ("examples/evals/outputs/frontend-state-contract.md", ".agent-ops/evals/outputs/frontend-state-contract.md"),
    ("examples/evals/outputs/data-freshness-contract.md", ".agent-ops/evals/outputs/data-freshness-contract.md"),
    ("examples/evals/outputs/external-action-governance.md", ".agent-ops/evals/outputs/external-action-governance.md"),
]


def copy_file(source: Path, target: Path, *, force: bool) -> str:
    if not source.is_file():
        raise FileNotFoundError(source)
    if target.exists() and not force:
        return f"skip existing {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return f"write {target}"


def init_target(target: Path, *, force: bool, demo: bool) -> list[str]:
    actions: list[str] = []
    for source_rel, target_rel in FILES_TO_COPY:
        actions.append(copy_file(ROOT / source_rel, target / target_rel, force=force))
    if demo:
        for source_rel, target_rel in DEMO_FILES:
            actions.append(copy_file(ROOT / source_rel, target / target_rel, force=force))
    readme = target / ".agent-ops" / "README.md"
    if force or not readme.exists():
        readme.parent.mkdir(parents=True, exist_ok=True)
        readme.write_text(
            "# Agent Ops\n\n"
            "This folder was initialized from the Agent Contract Tests.\n\n"
            "Start with:\n"
            "1. `.agent-ops/templates/governed-task.md`\n"
            "2. `.agent-ops/agents/orchestrator.md`\n"
            "3. `.agent-ops/registry/tool-acl.yaml`\n"
            "4. `python3 scripts/agent_ops_validate.py --strict`\n\n"
            "Keep real secrets, private prompts, and customer data out of this folder.\n"
        )
        actions.append(f"write {readme}")
    return actions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize Agent Ops starter files.")
    parser.add_argument("--target", help="Target repository path")
    parser.add_argument("--demo", action="store_true", help="Create a local demo under ./agent-ops-demo when --target is omitted")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.target:
        target = Path(args.target).expanduser().resolve()
        demo = args.demo
    elif args.demo:
        target = (ROOT / "agent-ops-demo").resolve()
        demo = True
    else:
        print("FAIL: pass --target <repo> or --demo", file=sys.stderr)
        return 1

    target.mkdir(parents=True, exist_ok=True)
    for action in init_target(target, force=args.force, demo=demo):
        print(action)
    print(f"OK initialized Agent Ops at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
