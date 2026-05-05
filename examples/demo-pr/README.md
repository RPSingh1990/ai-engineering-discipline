# Demo PR: Bad Agent Contract Fails CI

This repo maintains a demo branch that intentionally breaks the agent contract.

Expected failure:

- `product-manager` declares it can call `backend-builder`
- `call-graph.example.yaml` does not allow that route
- `scripts/agent_ops_validate.py --strict` fails CI

The point is to show the repo is not only documentation. A bad contract should fail before merge.

## Recreate Locally

```bash
git checkout -b demo/bad-agent-contract-fails-ci
python3 - <<'PY'
from pathlib import Path
path = Path("examples/software-team-agents/product-manager.md")
text = path.read_text()
path.write_text(text.replace(
    "allowed_callees: [orchestrator]",
    "allowed_callees: [orchestrator, backend-builder]",
))
PY
python3 scripts/agent_ops_validate.py --strict
```

Expected result:

```text
FAIL call graph enforcement
  - product-manager: allowed_callees exceed call graph ['backend-builder']
```
