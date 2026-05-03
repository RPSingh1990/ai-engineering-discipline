# Security Model

AI engineering systems fail when private execution details leak into public artifacts, frontends, logs, or downloadable templates.

This repository uses a public-safe model: publish useful patterns, never internal operating data.

## Do Not Publish

Never publish:

- API keys, tokens, passwords, cookies, refresh tokens
- `.env` files with real values
- raw private prompts or internal agent instructions
- memory paths, local machine paths, private repo paths
- customer names, client details, meeting notes
- production URLs that imply private access
- raw logs, screenshots, traces, or support data
- real tool ACLs or provider configs
- database connection strings
- private emails or relationship notes

## Safe To Publish

Safe public material:

- sanitized templates
- synthetic examples
- fake company names
- fake users
- fake API endpoints
- example call graphs
- example permission models
- public-safe case studies
- checklists
- validation scripts

## Public Agent Rule

Public agent examples should show:

- what the agent does
- when to use it
- inputs it needs
- outputs it produces
- guardrails
- escalation rules
- eval prompts

They should not show:

- raw internal prompts
- private memory structure
- actual internal registry files
- real tool bindings
- real secrets or access paths

## Governed Actions

These actions require explicit approval and audit evidence:

- sending email
- posting or commenting on social platforms
- deploying production
- deleting data
- changing auth
- spending money
- making trades or financial execution
- scraping or automating third-party accounts

The safe pattern is: draft, review, approve, execute, log.

## Pre-Publish Checklist

Before publishing a repo, run:

```bash
python3 scripts/validate_public_repo.py
```

Then manually check:

- no private names beyond intended public identity
- no real tokens in commit history
- no local absolute paths
- no raw internal agent files
- no customer/client details
- no screenshots with secrets

If any doubt exists, block release.

