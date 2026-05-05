# Scenario: Data Freshness And Provenance Failure

## Risk

The system merges multiple data sources without canonical identifiers, timestamps, source provenance, or quality gates.

## Required Agent Route

- data-engineer: define source inventory and contracts
- backend-builder: enforce validation and persistence rules
- security-reviewer: review sensitive/private data handling
- qa-reviewer: test stale and duplicate source behavior

## Contract Tests

- every entity has a canonical identifier
- every field has source provenance
- every record has retrieval timestamp
- stale data is flagged before downstream recommendations
- missing values are not silently filled

## Release Decision

Block until lineage and freshness checks exist.
