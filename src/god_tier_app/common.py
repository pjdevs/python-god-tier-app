"""God tier app common package including killer functions."""

import asyncio


async def hello() -> str:
    """Return a greeting message."""
    await asyncio.sleep(0.1)
    return "Hello from god-tier-app!"
