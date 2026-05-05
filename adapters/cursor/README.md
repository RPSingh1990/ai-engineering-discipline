# Cursor Adapter

Use this adapter when Cursor is working in a repository that has `.agent-ops/` installed.

## Setup

1. Initialize Agent Ops in the target repo.

   ```bash
   python3 scripts/agent_ops_init.py --target <repo> --demo
   ```

2. Create `.cursor/rules/agent-ops.mdc` in the target repo using the block below.

## `.cursor/rules/agent-ops.mdc`

```mdc
---
description: Apply Agent Ops contracts before AI-assisted engineering work.
alwaysApply: true
---

Before editing code, classify the work:

- Fast lane: tiny reversible docs/copy/local-only changes.
- Governed lane: auth, private data, data models, external actions, production deploys, payments, deletes, financial execution, or security-sensitive behavior.

For governed lane:

1. Use `.agent-ops/templates/governed-task.md`.
2. Respect `.agent-ops/registry/tool-acl.yaml`.
3. Respect `.agent-ops/registry/call-graph.yaml`.
4. Use only relevant agents from `.agent-ops/agents/`.
5. Keep file ownership explicit.
6. Run:

   ```bash
   python3 scripts/agent_ops_validate.py --strict
   python3 scripts/run_evals.py --eval-dir .agent-ops/evals
   ```

Do not bypass failed contract checks. Report the failing contract and ask for an explicit decision.
```

## CI

Copy `templates/agent-ops-validate.yml` into `.github/workflows/agent-ops-validate.yml`.
