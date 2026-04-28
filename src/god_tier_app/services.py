"""Module containing all services of the app."""

from wireup import injectable

from god_tier_app.common import SuperGreeter
from god_tier_app.settings import GodTierSettings


@injectable
async def get_settings() -> GodTierSettings:
    """Load configuration from environment variables."""
    return GodTierSettings()  # ty:ignore[missing-argument]


@injectable
async def get_greeter() -> SuperGreeter:
    """Hello service returning a greeting."""
    return SuperGreeter()
