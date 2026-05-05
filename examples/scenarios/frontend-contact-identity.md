# Scenario: Frontend Contact Identity Failure

## Risk

The app imports the wrong contact because search results match a name but not the supplied profile URL.

## Required Agent Route

- product-manager: define correct-person acceptance criteria
- frontend-builder: expose verification and failure states
- backend-builder: store canonical profile URL and source metadata
- qa-reviewer: test duplicate-name and wrong-link cases

## Contract Tests

- canonical profile URL is source of truth
- secondary search requires explicit identity comparison
- UI has loading, empty, error, permission, and mismatch states
- silent wrong-profile acceptance is blocked

## Release Decision

Approve with conditions only after wrong-person import becomes impossible or explicitly reviewable.
