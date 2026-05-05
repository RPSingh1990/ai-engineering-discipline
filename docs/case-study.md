# Failure Cases

This document is intentionally modest. It does not prove the toolkit works in every environment. It lists the failure classes the examples and deterministic evals currently cover.

## 1. Auth Trust Failure

Problem:

- UI claims a reset email was sent.
- Provider failed or was not configured.
- User receives no email.

Useful gate:

- provider success and failure are observable
- user messaging does not lie
- account enumeration is still protected
- reset tokens are never logged

Example:

- `examples/scenarios/auth-password-reset.md`

## 2. Frontend Identity Failure

Problem:

- a contact search accepts the wrong person
- name match wins over canonical profile URL
- UI has only the success state

Useful gate:

- canonical profile URL is source of truth
- secondary search requires identity comparison
- loading, empty, error, permission, mismatch, and success states exist

Example:

- `examples/scenarios/frontend-contact-identity.md`

## 3. Data Reliability Failure

Problem:

- pipeline merges sources without canonical IDs
- stale values are used as fresh values
- source provenance is missing

Useful gate:

- canonical identifier exists
- freshness threshold exists
- source provenance and lineage exist
- missing values are not silently filled

Example:

- `examples/scenarios/data-freshness-provenance.md`

## 4. External Action Failure

Problem:

- AI-generated draft becomes an email, social post, deploy, delete, or trade without human approval

Useful gate:

- draft and execution are separate
- approval evidence is required
- audit log and failure path exist
- runtime guard blocks missing evidence

Example:

- `examples/scenarios/external-action-governance.md`

## Current Limitation

These are examples and contract checks. They are not production proof. The next useful improvement is adapters for real agent runners.
