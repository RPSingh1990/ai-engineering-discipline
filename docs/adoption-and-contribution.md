# Adoption And Contribution

This repo should earn trust by being useful in real repositories, not by claiming novelty.

## Positioning

Use this angle:

> AI coding is useful. Unreviewed AI coding is the risk. This repo gives teams small contract tests for agent roles, permissions, eval outputs, and governed actions.

Avoid:

- "ultimate framework"
- "replace engineers"
- "enterprise ready"
- "10x with prompts"
- generic agent hype

## Honest Scope

This is not a replacement for AutoGen, CrewAI, LangGraph, AgentOps, Promptfoo, DeepEval, Inspect, Gitleaks, or a sandboxed runtime.

It is a lightweight repo-governance layer for teams that already use AI coding tools and need:

- task packets before large changes
- agent specs with narrow roles
- tool ACLs that CI can check
- call graphs that CI can check
- governed channels for send/post/deploy actions
- security and QA evidence before merge
- deterministic eval assertions over saved outputs

## Strong Contributions

The most useful contributions are concrete:

1. More enforcement checks in `scripts/agent_ops_validate.py`.
2. Better deterministic assertions in `scripts/run_evals.py`.
3. Better examples of governed tasks.
4. More failure modes from actual AI-assisted builds.
5. Adapters for common agent frameworks.

## Weak Contributions

Avoid:

- more generic agent names
- abstract principles without examples
- huge process documents
- raw private prompts
- fake enterprise claims

## Adoption Path

1. Run `python3 scripts/agent_ops_init.py --target <repo>`.
2. In the target repo, run `python3 scripts/agent_ops_validate.py --strict`.
3. Add one governed task for a real auth, data, deploy, or external-action change.
4. Open a PR and let the copied GitHub Action enforce the contracts.
5. Remove anything that feels like process weight without catching real risk.

## Public Launch Angle

If sharing the repo publicly, sell the problem and the workflow, not the author:

> Most AI engineering content teaches prompting or frameworks. I needed something smaller: a way to stop AI coding agents from drifting outside their jobs, tools, and review gates.
