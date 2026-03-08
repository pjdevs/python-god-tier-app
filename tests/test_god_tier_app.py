from dirty_equals import IsStr
from fastapi.testclient import TestClient
from hypothesis import given, settings
from hypothesis import strategies as st
from pytest_mock import MockerFixture

from god_tier_app.app import app, container
from god_tier_app.common import SuperGreeter, hello

client = TestClient(app)


async def test_hello():
    result = await hello()
    assert result == IsStr(regex=r"^Hello.*")


@given(st.text(min_size=1, max_size=20))
@settings(max_examples=10)
async def test_super_greeter(name: str):
    greeter = SuperGreeter()
    result = await greeter.greet(name)
    assert result == f"Hello, {name}!"


async def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == await hello()


async def test_greet(mocker: MockerFixture):
    # Arrange
    greeting = "Fake greeting"
    name = "World"
    mock_greeter = mocker.AsyncMock(spec=SuperGreeter)
    mock_greeter.greet.return_value = greeting

    # Make HTTP call
    with container.override.injectable(target=SuperGreeter, new=mock_greeter):
        response = client.get(f"/greet/{name}")

    # Assert HTTP
    assert response.status_code == 200
    assert response.json() == greeting

    # Assert internal calls
    mock_greeter.greet.assert_called_once_with(name)
    mock_greeter.greet.assert_awaited()
