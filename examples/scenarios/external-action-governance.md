# Scenario: External Action Governance Failure

## Risk

An AI workflow sends emails, posts to social media, deploys, deletes data, or executes financial actions without human approval.

## Required Agent Route

- product-manager: define user value and consent requirement
- security-reviewer: define approval and audit evidence
- backend-builder: enforce governed-channel checks
- devops-release: verify rollback and deployment evidence

## Contract Tests

- draft is allowed
- execution requires human approval
- approval evidence is recorded
- audit log and failure path exist
- runtime guard blocks missing evidence

## Release Decision

Block direct execution. Enable only draft-review-approve-execute-log.
