# Agent Contract Tests for AI-Assisted Engineering Teams

[![validate](https://github.com/RPSingh1990/ai-engineering-discipline/actions/workflows/validate.yml/badge.svg)](https://github.com/RPSingh1990/ai-engineering-discipline/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Small, runnable contract checks for teams using AI coding agents.

This repo is not an agent framework and not a claim of novelty. It is a lightweight way to turn agent roles, tool permissions, call graphs, governed actions, and eval assertions into files that can fail CI.

Use it beside Codex, Claude Code, Cursor, Copilot, AutoGen, CrewAI, LangGraph, or your own runner. The goal is simple: make agent behavior reviewable before it becomes production behavior.

## Who This Is For

Use this if you are:

- building with Codex, Claude Code, Cursor, GitHub Copilot, or other coding agents
- trying to move beyond "vibe coding" into repeatable engineering
- worried that AI-generated code will break as the product grows
- creating specialist agents such as PM, backend, frontend, QA, security, research, or code review
- trying to keep speed without losing architecture, security, and test discipline

## Core Idea

AI agents should be treated like employees, not magic prompts.

Each agent needs:

- a job description
- allowed inputs
- expected outputs
- permission boundaries
- escalation rules
- eval assertions
- evidence of performance
- a manager/orchestrator

The goal is not more agents. The goal is fewer, sharper agents with clear accountability.

## What Is Included

```text
docs/
  operating-model.md            How to run a small AI engineering team
  security-model.md             Public-safe and internal-safe boundaries
  evals-and-benchmarks.md       Lightweight eval discipline
  enforcement-model.md          What the validator enforces and what it cannot
  failure-modes.md              What breaks when AI coding scales badly
  prompt-blocks.md              Copy-paste prompts for Codex/Claude/Cursor
  case-study.md                 Multiple sanitized failure cases
  prior-art.md                  Related agent, eval, and security work
  adoption-and-contribution.md  Honest adoption path and contribution guide
  no-code-agent-ops.md          Operator-friendly use without writing code

examples/
  agents/                       Public-safe agent specifications
  software-team-agents/         Sanitized software-team agent pack
  registry/                     Example call graph, tool ACL, governed channels
  evals/                        Runnable deterministic eval assertions
  worked-example/               End-to-end governed task example
  scenarios/                    Four distinct failure scenarios
  before-after/                 Vibe-coded request vs governed agent task
  demo-repo/                    Minimal initialized Agent Ops example

templates/
  agent-request.md              Hire or upgrade an agent
  governed-task.md              Start governed engineering work
  security-review.md            Pre-release security review
  pr-checklist.md               AI-assisted PR checklist

scripts/
  validate_public_repo.py       Local/CI safety and structure checks
  agent_ops_init.py             Copy Agent Ops starter files into another repo
  agent_ops_validate.py         Enforce agent ACLs, call graph, and governed tasks
  agent_ops_guard.py            Runtime guard helpers for tool/call/channel checks
  run_evals.py                  Run deterministic assertions over saved outputs

.github/workflows/
  validate.yml                  GitHub Actions validation
.gitleaks.toml                  Gitleaks configuration
```

## Quick Start

Clone and run the validator:

```bash
python3 scripts/validate_public_repo.py
```

Expected result:

```text
PASS public safety scan
PASS required docs
PASS templates
PASS scripts
PASS security tooling
PASS agent examples
PASS software-team agent pack
PASS eval examples
```

Run the Agent Ops contract validator:

```bash
python3 scripts/agent_ops_validate.py --strict
```

Expected result:

```text
PASS agent specs
PASS tool ACL enforcement
PASS call graph enforcement
PASS governed channel registry
PASS governed tasks
```

Run deterministic eval assertions over saved agent outputs:

```bash
python3 scripts/run_evals.py
```

Expected result:

```text
RESULT 4/4 evals passed
```

Initialize Agent Ops files into another repo:

```bash
python3 scripts/agent_ops_init.py --target ../my-product
cd ../my-product
python3 scripts/agent_ops_validate.py --strict
```

Or generate a local demo:

```bash
python3 scripts/agent_ops_init.py --demo --force
python3 scripts/agent_ops_validate.py --root agent-ops-demo --strict
```

The initializer also copies a GitHub Action into the target repo so future PRs can fail when agent contracts drift.

## What Is Enforced

`scripts/agent_ops_validate.py` checks that:

- agents request only tools granted in `tool-acl.yaml`
- blocked tools are not requested or granted
- agent delegation matches `call-graph.yaml`
- governed channels define approval and evidence fields
- governed tasks include owner, lane, scope, reviews, tests, rollback, and evidence
- strict mode fails if registry permissions and agent specs drift

This is CI-time enforcement. It does not intercept live model tool calls. For runtime enforcement, wire the same registry files into your agent runner or tool middleware.

For a minimal runtime check:

```bash
python3 scripts/agent_ops_guard.py tool backend-builder repo_read
python3 scripts/agent_ops_guard.py call product-manager backend-builder
```

The first command should allow the tool. The second should deny the call because the example call graph routes implementation work through the orchestrator.

`scripts/run_evals.py` does not call a model. It scores saved outputs. Generate an answer with any AI coding agent, save it as an output file, and run the same deterministic assertions against it.

## 30-Minute Adoption Path

If you want to try this on a real repo today:

1. Run `python3 scripts/agent_ops_init.py --target <repo>`.
2. In the target repo, run `python3 scripts/agent_ops_validate.py --strict`.
3. Pick one real auth, email, deploy, data, or external-action change.
4. Write it as a governed task before asking agents to implement it.
5. Keep only the agents and tools you actually need.
6. Let the copied GitHub Action fail PRs when contracts drift.

For a complete example, read:

- `examples/worked-example/README.md`
- `examples/worked-example/agent-request.md`
- `examples/worked-example/governed-task.md`
- `examples/worked-example/sample-review.md`

For the sanitized software-team agent pack, read:

- `examples/software-team-agents/README.md`

## The Minimum Useful Workflow

1. Write an agent request before creating a new agent.
2. Define the agent with a narrow role and trigger.
3. Add 2-3 realistic eval assertions.
4. Give the agent the smallest useful permissions.
5. Route sensitive work through a security review.
6. Require evidence before merge or deploy.
7. Promote the agent only after real output is good.

## What This Is Not

This is not:

- an agent framework
- a model wrapper
- a prompt marketplace
- a complete sandbox
- a replacement for Gitleaks, GitHub secret scanning, Promptfoo, DeepEval, Inspect, or AgentOps
- a replacement for engineering judgment
- a way to bypass code review, security review, or tests

It is an Agent Ops layer for teams already using AI coding tools.

## Good First Use Cases

- Create a backend agent with API-contract discipline.
- Add a security reviewer before deployment.
- Add a PM agent that converts vague founder requests into acceptance criteria.
- Add a QA agent that checks behavior beyond the happy path.
- Add contract tests that block drift in agent tools, calls, eval outputs, and governed actions.

## Contribution Path

If this helps your team, fork it or open an issue with your own agent-operating pattern. The strongest contributions are concrete: better enforcement checks, eval assertions, governed-task examples, and failure cases from real AI-assisted builds.

## License

MIT. Use it, adapt it, and improve it.
