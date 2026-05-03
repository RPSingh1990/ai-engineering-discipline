# Sanitized Case Study: From Vibe Coding To Agent Ops

This case study is public-safe. It describes patterns from real AI-assisted product work without exposing private repo internals, customer data, credentials, raw prompts, or production configuration.

## Starting Problem

AI coding made it possible to build quickly, but speed introduced new risks:

- duplicated work across chats
- unclear ownership between agents
- frontend and backend drift
- weak deployment discipline
- shallow testing
- private details leaking into public-facing material
- too much orchestration for small tasks
- not enough governance for sensitive tasks

The problem was not that AI coding was useless. The problem was that AI coding without an operating model became hard to trust.

## Sanitized Failure Example

A password-reset feature looked complete from the UI:

- user entered email
- UI showed "reset email sent"
- backend returned success-like response

But the mail provider was not actually delivering the reset email. The product created a trust failure: the user was told an email had been sent when the system had no delivery evidence.

The engineering issue was not just "email bug." It was an AI-assisted delivery discipline failure:

- no provider-failure test
- no telemetry for delivery failure
- no clear user-facing distinction between safe account-enumeration protection and false delivery confirmation
- no release gate asking whether auth-sensitive flows had been tested end to end

## Intervention

The team moved this class of work into a governed lane:

1. PM defines the user trust requirement.
2. Backend defines exact provider success/failure behavior.
3. Security checks account-enumeration risk and false-success messaging.
4. QA tests success, unknown account, provider failure, rate limits, and expired token.
5. Release requires evidence before deploy.

## Measurable Improvement

The output changed from:

> "Looks done; the form says email sent."

to:

> "The reset flow is releasable only if provider success/failure is observable, tests cover failure states, and user messaging is honest without leaking whether the account exists."

That is the practical difference between AI-generated feature completion and production-grade engineering.

## What Changed

The system moved to a lightweight AI engineering discipline:

- one orchestrator owns synthesis
- specialists have narrow roles
- permissions are explicit
- external actions are governed
- security review blocks risky release paths
- every reusable agent has eval prompts
- benchmark evidence is tracked
- public artifacts are sanitized before release

## What Worked

Useful patterns:

- fast lane for tiny reversible tasks
- governed lane for product/security/release work
- stable agent IDs instead of cute names
- call graph to avoid uncontrolled loops
- tool ACLs to prevent broad access by default
- public-safe templates instead of private prompt dumps
- evals before promotion

## What Did Not Work

Weak patterns:

- treating every task as a multi-agent process
- making agent instructions longer instead of clearer
- exposing raw agent internals as public content
- assuming a successful demo means production readiness
- using a cheap model for judgment-heavy research without review
- building many products without explicit sequencing

## Practical Takeaway

AI engineering scales when the team treats agents as accountable workers:

- define the job
- limit the tools
- test the behavior
- review the output
- promote only with evidence

The discipline matters more than the prompt.
