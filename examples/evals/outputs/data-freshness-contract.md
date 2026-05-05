# Data Freshness Contract

## Decision

Block until the pipeline has canonical identifiers, freshness rules, and source provenance.

## Required Findings

- Each entity needs a canonical identifier before merge.
- Each field needs source provenance and retrieval timestamp.
- Freshness thresholds must be defined per source type.
- Lineage must preserve raw source values before transformations.
- Quality gate failures must stop downstream recommendations.
- Silent imputation is not allowed.

## Release Gate

Data engineering must provide duplicate handling, stale-source behavior, and reconciliation evidence.
