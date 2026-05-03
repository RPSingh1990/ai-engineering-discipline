#!/usr/bin/env python3
"""Regression checks for public-safety regexes."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_public_repo.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_public_repo", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def assert_matches(name: str, value: str) -> None:
    validator = load_validator()
    pattern = validator.FORBIDDEN_PATTERNS[name]
    assert pattern.search(value), f"{name} did not match"


def main() -> int:
    assert_matches("env_assignment_secret", "API" + "_KEY=abcdefghi12345")
    assert_matches("env_assignment_secret", "SECRET" + "=abcdefghi12345")
    assert_matches("database_url_value", "postgresql://user:" + "pass123456" + "@example.com/db")
    assert_matches("linkedin_cookie", "li" + "_at=AQE123456789")
    assert_matches("linkedin_cookie", "JSESSION" + "ID=ajax:123")
    print("PASS validator selftest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
