# Enforcement Model

This repo has two layers:

1. Human operating discipline: templates, task packets, review checklists, and eval prompts.
2. CI-time enforcement: scripts that fail when agent contracts drift from the registry.
3. Runtime guard helpers: small functions an agent runner can call before tools, delegation, or governed actions.

It does not claim to sandbox every agent runtime. That requires platform-specific middleware. The goal here is smaller and practical: make agent permissions reviewable, copyable, enforceable in a normal GitHub workflow, and easy to wire into a runner.

## What The Validator Enforces

Run:

```bash
python3 scripts/agent_ops_validate.py --strict
```

The validator checks:

- every agent has required fields and sections
- requested tools are granted in `tool-acl.yaml`
- blocked tools are not requested or granted
- `allowed_callees` match `call-graph.yaml`
- declared callers are permitted by the call graph
- governed channels contain approval and evidence fields
- governed task files include owner, lane, scope, reviews, tests, rollback, and evidence

## What It Does Not Enforce

It does not:

- intercept live model tool calls
- isolate processes or browser sessions
- replace secrets management
- prove an LLM followed instructions at runtime
- replace code review, tests, or security review

Those belong in the host agent runtime, sandbox, deployment platform, and engineering process.

## Why This Still Helps

Most teams start with agent prompts scattered across docs and chats. Nobody knows:

- which tools an agent is allowed to use
- which agent can call which specialist
- whether a high-risk action needs approval evidence
- whether the public agent file accidentally broadened permissions

This repo turns those assumptions into files that can fail CI.

## Target Repo Layout

After running `agent_ops_init.py`, the target repo gets:

```text
.agent-ops/
  agents/
  registry/
  templates/
  tasks/
scripts/
  agent_ops_validate.py
.github/workflows/
  agent-ops-validate.yml
```

The GitHub Action runs:

```bash
python3 scripts/agent_ops_validate.py --strict
```

## Strict Mode

Strict mode fails on drift:

- agent requests a tool not in ACL
- ACL grants a tool the agent did not declare
- agent calls another agent not in call graph
- call graph allows undeclared calls

Use strict mode for reusable agents and public examples. Use non-strict mode temporarily while migrating older repositories.

## Runtime Enforcement Path

Use `scripts/agent_ops_guard.py` as the minimal runtime hook:

```python
import sys

sys.path.append("scripts")
from agent_ops_guard import AgentOpsGuard

guard = AgentOpsGuard(".")
guard.assert_tool_allowed("backend-builder", "repo_read")
guard.assert_call_allowed("orchestrator", "backend-builder")
guard.assert_channel_evidence("email_send", evidence)
```

Then wire the same registry files into your agent runner:

1. Load `tool-acl.yaml` before tool execution.
2. Check `agent_id` plus requested tool against ACL.
3. Block tools listed under `blocked_tools`.
4. Check `call-graph.yaml` before one agent delegates to another.
5. Require governed-channel evidence before send/post/deploy actions.
6. Log every blocked decision.

The repo-level validator is the first gate. The guard is the small runtime bridge. Full sandboxing still belongs in your execution platform.
