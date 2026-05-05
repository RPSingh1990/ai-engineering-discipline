# No-Code Agent Ops

This repo is technical, but the operating model can be used by founders, product leaders, and operators who do not want to write code.

If you are fully no-code, use the templates and prompt block. The CLI requires Python and a repository, so it is meant for a technical teammate or AI coding environment.

## What You Can Use Without Coding

Use these templates directly in ChatGPT, Claude, Codex, Cursor, Linear, Notion, Google Docs, or a project tracker:

- `templates/agent-request.md`
- `templates/governed-task.md`
- `templates/security-review.md`
- `templates/pr-checklist.md`
- `docs/prompt-blocks.md`
- `examples/software-team-agents/`

## Copy-Paste Operating Prompt

```text
Act as my Agent Ops orchestrator.

I am using AI tools to build software. Before any agent writes code, create:
1. a governed task packet,
2. the agent roles needed,
3. permission boundaries,
4. acceptance criteria,
5. security review questions,
6. QA checks,
7. rollback plan.

Use fast lane only for tiny reversible work.
Use governed lane for auth, data, deploy, external actions, payments, private data, or production changes.
```

## Simple Workflow

1. Start with the governed-task template.
2. Fill in what you want built.
3. Ask your AI coding tool to classify the work as fast lane or governed lane.
4. If governed, ask it to use the relevant agent files from `examples/software-team-agents`.
5. Ask Security and QA to review before deploy.

## Operator Rule

Do not ask for "build everything."

Ask:

> What is the smallest complete release that gives value and can be safely reviewed?

That one sentence prevents most AI-build chaos.
