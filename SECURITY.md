# Security Policy

## Supported Versions

This project is pre-1.0. Security fixes apply to the latest commit on `main` and the latest tagged release.

## Reporting A Vulnerability

Do not open a public issue for secrets, private data exposure, bypasses in the validator, or unsafe examples.

Report privately by emailing the repository owner or using GitHub's private vulnerability reporting if it is enabled for this repository.

Include:

- affected file or command
- expected behavior
- observed behavior
- minimal reproduction
- whether any secret, private prompt, customer data, or local path was exposed

## Security Scope

In scope:

- secret-like content missed by `validate_public_repo.py`
- public examples that leak private paths, raw internal prompts, credentials, or customer details
- validator bypasses that allow unsafe agent contracts to pass
- governed-action checks that accept missing approval or evidence

Out of scope:

- sandbox escapes in third-party agent runtimes
- LLM jailbreaks outside this repository's deterministic checks
- vulnerabilities in GitHub Actions, Gitleaks, Promptfoo, DeepEval, Inspect, AgentOps, AutoGen, CrewAI, LangGraph, Codex, Claude Code, Cursor, or Copilot
- claims that require access to private systems or accounts

## Maintainer Commitments

- Treat security reports as confidential until resolved.
- Prefer small, auditable fixes over broad rewrites.
- Add regression coverage for accepted security fixes where practical.
- Keep public examples synthetic and free of private operational data.
