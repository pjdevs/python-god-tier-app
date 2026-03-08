FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

WORKDIR /app

# Only copy uv.lock and not pyproject.toml
# This ensures hermiticity of the build
# And prevents docker image invalidation in case non-dependency changes
# are made to pyproject.toml
COPY pyproject.toml README.md uv.lock ./
COPY src ./src

# Install dependencies
# virtual env is created in "/app/.venv" directory
RUN uv sync --no-dev --frozen --no-editable

FROM python:3.14-slim AS runner
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app/.venv/lib/python3.14/site-packages

WORKDIR /app
ENTRYPOINT ["uvicorn", "god_tier_app.app:app", "--host=0.0.0.0", "--port=8000"]
