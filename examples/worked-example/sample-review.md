# Sample Release Review

## PM Review

Decision: approve.

Reason: the fix improves user trust without expanding scope.

## Security Review

Decision: approve with conditions.

Required conditions:

- do not expose account existence
- do not log reset tokens
- do not claim email delivery when provider failed
- rate-limit reset requests

## QA Review

Decision: approve after tests pass.

Required checks:

- provider success
- provider failure
- unknown account
- timeout
- rate limit
- expired token

## Release Decision

Approved only after test evidence is attached.

