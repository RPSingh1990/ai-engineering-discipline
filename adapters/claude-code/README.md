# Claude Code Adapter

Use this adapter when Claude Code is working in a repository that has `.agent-ops/` installed.

## Setup

1. Run:

   ```bash
   python3 scripts/agent_ops_init.py --target <repo> --demo
   ```

2. Copy the prompt below into `CLAUDE.md` or the project instruction area used by your Claude Code workflow.

## CLAUDE.md Block

```md
# Agent Ops Contract

Before editing code, inspect `.agent-ops/`.

Use fast lane only for tiny reversible changes.
Use governed lane for auth, data, deploy, external actions, private data, payments, security-sensitive behavior, or production changes.

For governed work:

1. Create or update a governed task packet under `.agent-ops/tasks/`.
2. Use only agents listed under `.agent-ops/agents/`.
3. Respect `.agent-ops/registry/tool-acl.yaml`.
4. Respect `.agent-ops/registry/call-graph.yaml`.
5. Do not send, post, deploy, delete, trade, or execute external actions without approval evidence.
6. Run:

   ```bash
   python3 scripts/agent_ops_validate.py --strict
   python3 scripts/run_evals.py --eval-dir .agent-ops/evals
   ```

If a requested action is blocked by Agent Ops policy, report the blocker and do not bypass it.
```

## CI

Copy `templates/agent-ops-validate.yml` into `.github/workflows/agent-ops-validate.yml`.
