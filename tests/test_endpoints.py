from http import HTTPStatus

from pytest import fixture
from starlette.testclient import TestClient

from application.main import app
from tests.factories import GameFactory


@fixture
def client() -> TestClient:
    return TestClient(app)


def test_returns_501_on_get_all_games(client: TestClient) -> None:
    result = client.get("/games/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code


def test_returns_501_on_get_game(client: TestClient) -> None:
    game = GameFactory()
    result = client.post(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code
