# Worked Example: Password Reset Trust Gate

This is a synthetic example showing how a governed task moves through the discipline.

Scenario:

An app has a password-reset screen. The UI says "reset email sent" even when the email provider fails. The team wants to fix it without leaking whether an account exists.

Flow:

1. `agent-request.md`: asks whether a backend/security agent is needed.
2. `governed-task.md`: defines scope and reviews.
3. `evals.json`: tests expected behavior.
4. `sample-agent-output.md`: shows a good backend/security response.
5. `sample-review.md`: shows the release decision.

Why this matters:

This is a small feature, but it touches auth, email, trust, telemetry, and user support. It should not be treated as a casual UI copy change.

