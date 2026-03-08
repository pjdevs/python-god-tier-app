"""God tier app common package including killer functions."""

import asyncio


async def hello() -> str:
    """Return a greeting message."""
    await asyncio.sleep(0.1)
    return "Hello from god-tier-app!"


def super_sum(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
