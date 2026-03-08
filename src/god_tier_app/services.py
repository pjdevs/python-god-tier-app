"""Module containing all services of the app."""

from wireup import injectable

from god_tier_app.common import SuperGreeter


@injectable
async def get_greeter() -> SuperGreeter:
    """Hello service returning a greeting."""
    return SuperGreeter()
