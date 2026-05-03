# Governed Task: Password Reset Trust Gate

## Summary

Fix password-reset behavior so user messaging is honest and safe when the mail provider fails.

## Owner

Orchestrator / CTO

## Lane

`governed`

## Why Governed

- auth
- external email provider
- user trust
- security-sensitive messaging

## Scope

In scope:

- backend provider-result handling
- safe response contract
- telemetry for provider failures
- frontend message states if needed
- tests

Out of scope:

- changing auth provider
- changing email vendor
- sending real emails in tests
- redesigning the whole login flow

## Required Reviews

- PM: confirm trust requirement
- Backend: implement contract
- Security: review account-enumeration and token/log risk
- QA: test all reset states

## Acceptance Criteria

1. Provider success records delivery attempt evidence.
2. Provider failure does not falsely say delivery succeeded.
3. Unknown account response does not expose whether account exists.
4. Reset tokens are never logged.
5. Tests cover provider success, provider failure, unknown account, rate limit, and expired token.

## Test Plan

```bash
pytest tests/auth/test_password_reset.py
python3 scripts/validate_public_repo.py
```

## Rollback Plan

Revert endpoint and frontend state changes. Keep provider failure logs for diagnosis if safe.

## Evidence

- test output
- security review
- QA checklist

