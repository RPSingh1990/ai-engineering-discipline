# Agent Request: Auth Flow Review

## Request Type

`use_existing_agent`

## Agent

- agent_id: backend-builder
- secondary_review: security-reviewer
- reports_to: orchestrator
- risk_level: medium
- data_classification: internal

## Business Need

Fix a password-reset trust bug where the UI claims a reset email was sent even when delivery failed.

## Why Existing Direct Execution Is Not Enough

The work touches auth, provider failure, account-enumeration risk, user messaging, telemetry, and tests. It needs backend and security judgment.

## Inputs

- current password-reset endpoint behavior
- email provider result contract
- existing auth tests
- frontend message states

## Outputs

- corrected backend behavior
- safe user messaging
- telemetry requirements
- test cases
- release decision

## Permissions Requested

- tools: repo_read, repo_write_backend, run_backend_tests
- memory_scope: task_relevant_only
- write_scope: auth_backend_files_only
- external_actions: none

## Guardrails

- do not send real emails during tests
- do not expose whether an account exists
- do not claim delivery when provider delivery failed
- do not log reset tokens

## Evals

1. Provider success.
2. Provider failure.
3. Unknown account.

## Rollback Plan

Revert endpoint changes and restore previous frontend copy while keeping telemetry disabled.

