"""God tier app FastAPI app module including killer routes."""

from typing import TYPE_CHECKING

from fastapi import FastAPI
from wireup.integration.fastapi import setup

if TYPE_CHECKING:
    from wireup import Injected

from god_tier_app.common import SuperGreeter, hello
from god_tier_app.di import container

app = FastAPI()


@app.get("/")
async def index() -> str:
    """Index route returning greetings."""
    return await hello()


@app.get("/greet/{name}")
async def greet(name: str, greeter: Injected[SuperGreeter]) -> str:
    """Greet route returning a personalized greeting."""
    return await greeter.greet(name)

setup(container, app)
