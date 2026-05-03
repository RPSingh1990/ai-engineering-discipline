# Operating Model

This model is for small teams using AI agents to build real software. It keeps the speed of AI coding while preserving accountability.

## The Team Shape

Use one orchestrator and a small number of specialists.

```text
Founder / Product Owner
  -> Orchestrator / CTO
       -> Product Manager
       -> Architecture
       -> Backend
       -> Frontend
       -> Database
       -> QA
       -> Security
       -> Code Review
       -> Research
```

The orchestrator owns final synthesis. Specialists do not create uncontrolled loops.

## Two Lanes

### Fast Lane

Use for tiny, reversible work:

- copy edits
- simple docs
- small UI polish
- local-only scripts
- low-risk refactors

Rules:

- one agent or direct execution
- no production deploy
- no sensitive data
- no external action

### Governed Lane

Use for product/code/security/release work:

- auth
- data model changes
- production deploys
- external integrations
- email/post/send workflows
- private data
- payments or cost-bearing actions
- anything that affects customer trust

Rules:

- clear task packet
- owner
- security review when needed
- tests or explicit test waiver
- rollback plan
- evidence before merge/deploy

## Agent Contract

Every reusable agent should define:

- `agent_id`: stable machine ID
- `description`: trigger-aware summary
- `reports_to`: manager/orchestrator
- `allowed_callers`: who may invoke it
- `allowed_callees`: who it may ask for help
- `tools`: smallest useful set
- `memory_scope`: what context it may read
- `write_scope`: what it may change
- `output_contract`: expected output shape
- `evals`: realistic test prompts

## Parallel Work Rule

Parallel agents are useful when:

- tasks are independent
- file ownership is separate
- no unresolved decision blocks them
- the orchestrator can merge outputs

Do not run agents in parallel when:

- they edit the same files
- they need the same unresolved decision
- they repeat the same analysis
- the task is smaller than the orchestration cost

## Escalation Rule

Agents escalate upward when:

- required inputs are missing
- tool permissions are insufficient
- security risk is unclear
- a new dependency or architecture change is needed
- external action is requested
- output confidence is low

Escalation is not failure. It is how the system avoids silent bad assumptions.

## Promotion Rule

Do not give an agent more authority because it exists.

Promote only after:

- realistic evals pass
- real work output is reviewed
- permission scope is still narrow
- failure behavior is understood
- security has no blockers

