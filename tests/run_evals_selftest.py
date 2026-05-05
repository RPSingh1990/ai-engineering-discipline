#!/usr/bin/env python3
"""Regression tests for deterministic eval runner."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, check=False, capture_output=True, text=True)


def main() -> int:
    good = run(["python3", "scripts/run_evals.py"])
    assert good.returncode == 0, good.stdout + good.stderr
    assert "RESULT" in good.stdout, good.stdout

    with tempfile.TemporaryDirectory() as temp_dir:
        eval_dir = Path(temp_dir)
        (eval_dir / "bad-output.md").write_text("This output misses the required term.")
        (eval_dir / "bad.json").write_text(
            json.dumps(
                {
                    "agent_id": "selftest",
                    "evals": [
                        {
                            "name": "expected_failure",
                            "prompt": "Return a safe approval gate.",
                            "output_file": "bad-output.md",
                            "assertions": [{"type": "contains", "value": "human approval"}],
                        }
                    ],
                }
            )
        )
        bad = run(["python3", "scripts/run_evals.py", "--eval-dir", str(eval_dir)])
        assert bad.returncode != 0, "bad eval should fail"
        assert "FAIL" in bad.stdout, bad.stdout

    print("PASS run evals selftest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
