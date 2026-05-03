# Contributing

Useful contributions are concrete and public-safe.

Good contributions:

- new eval prompts
- improved validation checks
- better templates
- realistic failure modes
- public-safe agent examples
- documentation clarifications

Do not contribute:

- real secrets
- private prompts
- customer data
- internal logs
- screenshots with private data
- exploit code
- instructions for bypassing platform rules

Before opening a PR:

```bash
python3 scripts/validate_public_repo.py
```

If your contribution changes agent examples or templates, explain the problem it solves and the failure mode it prevents.

