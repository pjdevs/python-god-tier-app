from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from god_tier_app.app import app, container
from god_tier_app.common import SuperGreeter, hello

client = TestClient(app)


async def test_hello():
    result = await hello()
    assert result.startswith("Hello")


async def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == await hello()


async def test_greet(mocker: MockerFixture):
    # Arrange
    mock_greeter = mocker.AsyncMock(spec=SuperGreeter)
    mock_greeter.greet.return_value = "Greet"

    # Make HTTP call
    with container.override.injectable(target=SuperGreeter, new=mock_greeter):
        response = client.get("/greet/World")

    # Assert HTTP
    assert response.status_code == 200
    assert response.json() == "Greet"

    # Assert internal calls
    mock_greeter.greet.assert_called_once_with("World")
    mock_greeter.greet.assert_awaited()
