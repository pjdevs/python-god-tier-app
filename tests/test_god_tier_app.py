from god_tier_app.common import hello


async def test_hello():
    result = await hello()
    assert result.startswith("Hello")
