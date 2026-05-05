# Prior Art

This repo is not claiming the agent-governance idea is new. It is a small implementation layer that borrows from established work and makes a few checks runnable in ordinary repositories.

## Agent Design And Orchestration

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents/) is the best starting point for deciding when to use simple workflows versus agents.
- [Microsoft AutoGen](https://github.com/microsoft/autogen) provides a framework for multi-agent applications and agent conversations.
- [CrewAI](https://docs.crewai.com/en/index) provides agents, crews, flows, and integrations for multi-agent workflows.
- [LangGraph](https://docs.langchain.com/langgraph) focuses on long-running, stateful agent workflows and production deployment patterns.

## Agent Observability

- [AgentOps](https://docs.agentops.ai/) focuses on observability, monitoring, session recording, and replay for agent systems.

This repo does not replace those tools. It provides repository-level contracts that can sit beside them.

## LLM And Agent Evaluation

- [Promptfoo](https://www.promptfoo.dev/docs/intro/) provides declarative LLM evals and red-team testing.
- [DeepEval](https://deepeval.com/docs/introduction) provides LLM evaluation metrics and LLM-as-judge workflows.
- [Inspect AI](https://inspect.aisi.org.uk/) provides an eval framework for large language model evaluations.
- [Giskard](https://docs.giskard.ai/) provides LLM testing, evaluation, and red-team tooling.

The eval runner here is intentionally smaller. It performs deterministic checks on saved agent outputs. Use a mature eval framework when you need model execution, judge models, datasets, or experiment tracking.

## Security Baselines

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) is the baseline reference for LLM application risks.
- [Gitleaks](https://github.com/gitleaks/gitleaks) is a mature open-source secret scanner.
- GitHub native secret scanning should be enabled on public repositories where available.

The local regex scanner in this repo is a last-mile public-safety check. It is not a replacement for Gitleaks, GitHub secret scanning, code review, or threat modeling.

## What This Repo Adds

The useful wedge is narrow:

- machine-readable agent specs
- tool ACL checks
- call graph checks
- governed-channel evidence checks
- deterministic eval assertions over saved outputs
- a tiny runtime guard that can be wired into an agent runner

If a future version does not improve those concrete checks, it should not add more docs.
