"""God tier app FastAPI app module including killer routes."""

from fastapi import FastAPI

from god_tier_app.common import hello

app = FastAPI()


@app.get("/")
async def index() -> str:
    """Index route returning greetings."""
    return await hello()
