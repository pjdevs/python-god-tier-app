FROM ghcr.io/astral-sh/uv:bookworm-slim AS builder

WORKDIR /app

# Only copy uv.lock and not pyproject.toml
# This ensures hermiticity of the build
# And prevents docker image invalidation in case non-dependency changes
# are made to pyproject.toml
COPY uv.lock /app

# Install dependencies
# virtual env is created in "/app/.venv" directory
RUN uv init --name god_tier_app && uv sync --no-dev --frozen

FROM python:3.14-slim AS runner
COPY src /app/src
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app/.venv/lib/python3.14/site-packages
WORKDIR /app
ENTRYPOINT ["python", "src/god_tier_app/__init__.py"]