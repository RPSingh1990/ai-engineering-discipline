# Evals And Benchmarks

The files in `examples/evals/` are runnable deterministic evals, not model benchmarks.

They answer a narrow question:

> Given an agent output, did it include the contract-critical findings we expected?

They do not answer:

- which model is best
- whether the agent solved the full task
- whether an LLM judge would prefer the output
- whether the code compiles

Use Promptfoo, DeepEval, Inspect, Giskard, LangSmith, or another mature eval system when you need model execution, judge models, datasets, traces, or experiment tracking.

## Run The Included Evals

```bash
python3 scripts/run_evals.py
```

The eval runner loads JSON files from `examples/evals/`, reads each saved output file, and applies assertions such as:

- `contains`
- `not_contains`
- `contains_all`
- `contains_any`
- `regex`
- `heading`
- `min_word_count`

## Eval File Shape

```json
{
  "schema_version": "agent-contract-eval-v1",
  "agent_id": "software-team",
  "evals": [
    {
      "name": "external_action_governance",
      "prompt": "Review an AI workflow that sends emails directly after drafting content.",
      "output_file": "outputs/external-action-governance.md",
      "assertions": [
        {"type": "contains", "value": "human approval"},
        {"type": "not_contains", "value": "autopost"}
      ]
    }
  ]
}
```

## How To Use With A Real Agent

1. Ask the agent to respond to the prompt.
2. Save the response to the `output_file` path.
3. Run `python3 scripts/run_evals.py`.
4. Treat failures as review signals, not absolute truth.

## Current Example Coverage

The included evals cover four distinct failure classes:

- auth trust failure: password reset provider failure
- frontend correctness: wrong contact/profile accepted silently
- data reliability: missing canonical identifiers and freshness checks
- external action governance: AI drafts must not auto-send or auto-post

## Promotion Rule

Do not promote an agent because it has a nice role file.

Promote only when:

- it passes deterministic evals
- a human review agrees the output is useful
- the agent did not broaden its permissions
- security and QA review are satisfied for governed work

## Known Limitations

These evals are intentionally simple. They can be gamed by keyword stuffing. For serious model evaluation, add:

- negative examples
- hidden test cases
- LLM-as-judge scoring
- baseline comparison
- cost and latency tracking
- real code/test execution
