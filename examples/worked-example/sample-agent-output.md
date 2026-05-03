# Sample Agent Output

## Decision

Approve with conditions.

## Backend Contract

`POST /auth/password-reset/request`

Response states:

- `accepted_for_processing`: request accepted without exposing account existence
- `provider_delivery_confirmed`: internal event only, not exposed as account proof
- `provider_delivery_failed`: internal event plus safe user-facing recovery path

## User Messaging

Use safe wording:

> If we can process this request, you will receive reset instructions. If nothing arrives, wait a few minutes and try again.

When the provider fails for a known account, show:

> We could not complete the reset request right now. Please try again in a few minutes.

Do not say "email sent" unless the provider returned a successful send result.

## Telemetry

Log:

- request id
- provider status
- provider error class
- timestamp
- rate-limit state

Do not log:

- reset token
- raw email body
- provider secret

## Tests

Required:

- known account + provider success
- known account + provider failure
- unknown account
- rate limited request
- expired token
- provider timeout

## Escalation

Escalate to Security if product wants identical user copy for all provider states, because that may hide operational failure from the user.

