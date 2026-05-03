# Failure Modes

These are common ways AI-assisted engineering breaks after the demo.

## 1. The Product Works Only In The Happy Path

Symptoms:

- no empty states
- no error behavior
- no timeout handling
- no permission-state handling
- no rollback plan

Control:

- require QA prompts for non-happy paths
- require acceptance criteria before implementation
- block release if errors are generic or misleading

## 2. Agents Duplicate Work

Symptoms:

- multiple agents inspect the same files
- repeated architecture analysis
- repeated security commentary without new evidence
- token spend grows but confidence does not

Control:

- use one orchestrator
- assign file ownership
- define decision locks
- parallelize only independent work

## 3. Private Context Leaks Into Public Artifacts

Symptoms:

- raw prompts published as templates
- internal repo paths in docs
- screenshots contain private data
- examples mention real customers
- `.env` or logs included accidentally

Control:

- synthetic examples only
- pre-publish scan
- manual security review
- no raw internal agent files in public repos

## 4. Cheap Research Creates Expensive Mistakes

Symptoms:

- low-quality model summarizes weak sources
- stale or duplicate links are treated as insight
- source credibility is not scored
- content sounds plausible but is wrong

Control:

- deterministic source filters
- freshness checks
- credibility scoring
- "no strong result found" allowed
- human review for external-facing claims

## 5. Tool Access Becomes Convenience Access

Symptoms:

- agents request broad repo access
- send/post/deploy tools are exposed by default
- memory scope is larger than the task
- secrets are readable by too many actors

Control:

- default deny
- tool ACL
- governed channels
- approval metadata for external actions

## 6. More Process Slows Everything

Symptoms:

- every typo fix needs orchestration
- tiny docs updates require full review
- agents spend more time coordinating than building

Control:

- fast lane for reversible work
- governed lane only for sensitive work
- one-agent default
- explicit escalation triggers

## 7. Agent Instructions Become Bloated

Symptoms:

- every failure adds more rules
- agents become generic and cautious
- domain skill gets buried under process text

Control:

- keep role files lean
- use references for long standards
- add evals before adding instructions
- use scripts for deterministic checks

## 8. Demos Are Mistaken For Production

Symptoms:

- no observability
- no auth tests
- no data migration plan
- no deploy verification
- no rollback plan

Control:

- release checklist
- security review
- QA gate
- smoke test
- deployment evidence

