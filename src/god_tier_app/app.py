"""God tier app FastAPI app module including killer routes."""

from fastapi import FastAPI
from wireup import Injected
from wireup.integration.fastapi import setup

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
