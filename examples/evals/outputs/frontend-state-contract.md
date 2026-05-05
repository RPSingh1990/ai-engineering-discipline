# Frontend State Contract

## Decision

Approve with conditions only after state coverage and identity verification are explicit.

## Required Findings

- The UI must handle loading, empty, error, success, and permission states.
- A LinkedIn/contact import must treat the canonical profile URL as the source of truth.
- If secondary search is needed, the flow must compare name, image, company, education, and location before accepting a match.
- Silent wrong-profile acceptance is a release blocker.

## Release Gate

QA must test wrong-link, duplicate-name, private-profile, network-error, and permission-denied paths.
