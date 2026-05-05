# Scenario: Auth Password Reset Provider Failure

## Risk

The UI claims a reset email was sent even when the provider failed.

## Required Agent Route

- product-manager: define honest user messaging
- backend-builder: define provider success/failure contract
- security-reviewer: check account-enumeration and token logging
- qa-reviewer: test success and failure states

## Contract Tests

- provider failure is observable
- reset token is never logged
- unknown account does not reveal account existence
- rate limit and expired token paths are covered

## Release Decision

Block until tests and telemetry prove the flow is honest and safe.
