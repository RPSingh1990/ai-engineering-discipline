# Codex Adapter

Use this adapter when Codex is working in a repository that has `.agent-ops/` installed.

## Setup

1. Initialize Agent Ops in the target repo.

   ```bash
   python3 scripts/agent_ops_init.py --target <repo> --demo
   ```

2. Add the block below to the repo's `AGENTS.md`, `README.md`, or Codex project instructions.

## AGENTS.md Block

```md
# Agent Ops Contract

Before implementation, check whether the request is fast lane or governed lane.

Fast lane:
- docs, copy, tiny reversible edits
- no private data
- no production deploy
- no external action

Governed lane:
- auth
- data model or pipeline changes
- production deploy
- email/send/post/delete/trade/payment workflows
- private data
- security-sensitive behavior

For governed lane:

1. Read `.agent-ops/registry/tool-acl.yaml` and `.agent-ops/registry/call-graph.yaml`.
2. Keep file ownership explicit.
3. Use the smallest relevant specialist role from `.agent-ops/agents/`.
4. Run:

   ```bash
   python3 scripts/agent_ops_validate.py --strict
   python3 scripts/run_evals.py --eval-dir .agent-ops/evals
   ```

5. Stop if the contract validator fails.
6. Do not widen tool, memory, or write scope without updating the governed task and passing review.
```

## Runtime Guard

If Codex is controlling a custom runner, call `scripts/agent_ops_guard.py` before tool execution, delegation, or governed-channel actions.
