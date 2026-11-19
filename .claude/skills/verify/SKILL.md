---
name: verify
description: Prove a change to django-semolina works end to end. Use before saying a change is done, before committing, and before opening or updating a pull request.
---

# Verify a change

Run from the repository root:

```bash
uv sync --locked --dev
uv tool install prek  # once; skip if prek is already on PATH
prek run --all-files
CI=true uv run pytest
CI=true uv run --with 'django~=5.2.0' pytest
```

It passes when every command exits 0. The last line runs the suite on the Django 5.2 LTS
floor with your current Python, as CI's newest-Python job does. The lock already pairs
Python 3.11 with Django 5.2 and 3.12+ with Django 6.x.

`CI=true` turns on `tests/ci_skips.py`, which fails the run on any skip not allowed
there, as CI does. Without it a skipped test only shows in the summary, and a run that
skipped what you changed is not a pass. It is set on each test line rather than
exported, so it still holds when each line runs in a fresh shell, and other tools that
read `CI` keep their local behaviour.

Take each command's exit status from the command itself. In a pipeline `$?` is the last
command's status, so `cmd | tail` hides a failure. Redirect long output to a file, then
read the file.

## What this covers

- the package, its tests and the quality gates (ruff, basedpyright strict, uv lock)
- the oldest and newest supported Django on the Python you ran

## What it does not cover

- Python versions other than the one you ran: CI runs 3.11 and 3.14
- the docs build: run `just docs-build` when the change touches `docs/` or docstrings

## When it fails

- Read the first failure and fix its cause. Do not rerun hoping for a green, and do not
  skip, loosen or delete the failing test to get one.
- If the failure is real but outside the change, say so in the PR and in your report
  rather than working around it.
