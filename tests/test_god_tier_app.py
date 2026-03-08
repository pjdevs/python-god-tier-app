from fastapi.testclient import TestClient

from god_tier_app.app import app
from god_tier_app.common import hello

client = TestClient(app)


async def test_hello():
    result = await hello()
    assert result.startswith("Hello")


async def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == await hello()
