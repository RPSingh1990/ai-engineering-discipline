# Before: Vibe-Coded Feature

Prompt:

> Build password reset. User enters email, gets reset link, changes password.

Likely AI output:

- creates UI form
- creates backend endpoint
- sends email if configured
- stores token
- shows "email sent"

Hidden gaps:

- no provider failure behavior
- no account-enumeration check
- no token logging check
- no rate limiting
- no QA matrix
- no rollback plan
- no evidence that the reset email actually sends

Problem:

The feature can look complete while being unsafe or broken in production.

