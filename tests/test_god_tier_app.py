from god_tier_app import hello


def test_hello():
    assert hello().startswith("Hello")
