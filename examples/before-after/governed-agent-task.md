# After: Governed Agent Task

Prompt:

> Build password reset using Agent Ops. Classify risk, create a governed task, involve backend/security/QA, and do not claim email delivery unless provider success is observable.

Expected workflow:

1. Orchestrator classifies this as governed because it touches auth and email.
2. PM defines the trust requirement.
3. Backend defines provider success/failure contract.
4. Security reviews account enumeration, token handling, and logs.
5. QA tests success, unknown account, provider failure, timeout, rate limit, and expired token.
6. Release requires evidence and rollback plan.

Output:

- task packet
- backend contract
- security review
- QA checklist
- release decision

Result:

The feature is slower than a raw prompt, but much less likely to ship fake readiness.

