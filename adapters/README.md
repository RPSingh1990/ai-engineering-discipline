# Adapters

These adapters are small instruction blocks for common AI coding environments.

They do not magically enforce policy inside the model. Enforcement comes from:

- CI: `scripts/agent_ops_validate.py --strict`
- deterministic eval checks: `scripts/run_evals.py`
- optional runtime hooks: `scripts/agent_ops_guard.py`
- the composite GitHub Action in `action.yml`

## Included

- `claude-code/README.md`
- `codex/README.md`
- `cursor/README.md`

## Recommended Use

1. Initialize Agent Ops in a target repo.
2. Copy the matching adapter instruction into that tool's project-instruction mechanism.
3. Add the GitHub Action workflow from `templates/agent-ops-validate.yml`.
4. Treat failed checks as blockers unless a human explicitly changes the contract.
