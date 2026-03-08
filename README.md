# God Tier App

![CI Status](https://github.com/pjdevs/python-god-tier-app/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-91%25-green)
![License](https://badgen.net/github/license/pjdevs/python-god-tier-app)

Modern Python with Rust vibes.

## Install dependencies

```sh
uv venv
uv sync --all-extras --dev
```

## Lint

```sh
uv run ruff check
```

## Format

```sh
uv run ruff format
```

## Type check

```sh
uv run pyright
```

## Test

```sh
uv run pytest
```

## Pre-commit hooks

```sh
uv run pre-commit install
```

## Run

```sh
uv run uvicorn god_tier_app.app:app
```

## Package

```sh
uv build
```
