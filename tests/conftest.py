"""Shared pytest fixtures for django_semolina test suite."""

# Under CI, a skipped test fails the run (tests/ci_skips.py).
pytest_plugins = ["tests.ci_skips"]
