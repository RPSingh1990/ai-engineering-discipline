# AI Engineering Discipline

Practical guardrails for building software with AI agents without letting the system collapse into prompt sprawl, hidden security risk, or unreviewable code.

This repository is a public-safe toolkit distilled from real AI product-building work across:

- a personal AI operating system
- a relationship/productivity application
- a public agent showcase site
- a research decision-support prototype

It does not publish private prompts, internal memory, secrets, customer data, repo paths, production configs, or raw agent instructions. The examples here are sanitized patterns that a team can copy safely.

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
- eval prompts
- evidence of performance
- a manager/orchestrator

The goal is not more agents. The goal is fewer, sharper agents with clear accountability.

## What Is Included

```text
docs/
  operating-model.md            How to run a small AI engineering team
  security-model.md             Public-safe and internal-safe boundaries
  evals-and-benchmarks.md       Lightweight eval discipline
  failure-modes.md              What breaks when AI coding scales badly
  prompt-blocks.md              Copy-paste prompts for Codex/Claude/Cursor
  case-study.md                 Sanitized field notes from real builds
  recognition-plan.md           How to grow trust around the repo

examples/
  agents/                       Public-safe agent specifications
  registry/                     Example call graph, tool ACL, governed channels
  evals/                        Copyable eval prompts
  worked-example/               End-to-end governed task example

templates/
  agent-request.md              Hire or upgrade an agent
  governed-task.md              Start governed engineering work
  security-review.md            Pre-release security review
  pr-checklist.md               AI-assisted PR checklist

scripts/
  validate_public_repo.py       Local/CI safety and structure checks

.github/workflows/
  validate.yml                  GitHub Actions validation
```

## Quick Start

Clone and run the validator:

```bash
python3 scripts/validate_public_repo.py
```

Expected result:

```text
PASS public safety scan
PASS agent examples
PASS required docs
PASS templates
```

Then copy one template:

```bash
cp templates/agent-request.md my-agent-request.md
```

Use it to define a new agent before giving it tools or project access.

## 30-Minute Adoption Path

If you want to try this on a real repo today:

1. Copy `templates/pr-checklist.md` into your repo as `.github/PULL_REQUEST_TEMPLATE.md`.
2. Copy `templates/security-review.md` into `docs/security-review-template.md`.
3. Copy one agent example from `examples/agents/`.
4. Add one eval file from `examples/evals/`.
5. Run `python3 scripts/validate_public_repo.py` before publishing any public agent content.
6. Use the governed task template for your next auth, email, deploy, or data-model change.

For a complete example, read:

- `examples/worked-example/README.md`
- `examples/worked-example/agent-request.md`
- `examples/worked-example/governed-task.md`
- `examples/worked-example/sample-review.md`

## The Minimum Useful Workflow

1. Write an agent request before creating a new agent.
2. Define the agent with a narrow role and trigger.
3. Add 2-3 realistic eval prompts.
4. Give the agent the smallest useful permissions.
5. Route sensitive work through a security review.
6. Require evidence before merge or deploy.
7. Promote the agent only after real output is good.

## What This Is Not

This is not:

- an agent framework
- a model wrapper
- a prompt marketplace
- a replacement for engineering judgment
- a way to bypass code review, security review, or tests

It is a discipline layer for teams already using AI coding tools.

## Good First Use Cases

- Create a backend agent with API-contract discipline.
- Add a security reviewer before deployment.
- Add a PM agent that converts vague founder requests into acceptance criteria.
- Add a QA agent that checks behavior beyond the happy path.
- Add a repo validator that blocks leaked secrets and unsafe agent permissions.

## Recognition Path

If this helps your team, star the repo, fork it, or open an issue with your own agent-operating pattern. The strongest contributions are concrete examples: eval prompts, better security checks, useful templates, and failure cases from real AI-assisted builds.

## License

MIT. Use it, adapt it, and improve it.
