# External Action Governance

## Decision

Block direct external actions from AI drafts.

## Required Findings

- Email, social post, deploy, delete, and financial execution paths require human approval.
- The workflow must record approved_by, approved_at, evidence reference, audit log, and failure path.
- Social content should store a content hash before approval.
- The system must enforce no auto-send and no auto-post behavior by default.
- Drafting is allowed; execution is governed.

## Release Gate

Security must verify the governed channel evidence before any external action is enabled.
