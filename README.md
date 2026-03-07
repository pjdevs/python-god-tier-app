# God Tier App

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

## Build

```sh
uv build
```