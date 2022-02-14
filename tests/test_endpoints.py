from http import HTTPStatus

import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient

from application.main import app
from tests.factories import GameFactory


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.mark.asyncio
async def test_returns_501_on_get_all_games(client: TestClient) -> None:
    async with AsyncClient(app=app, base_url="http://test") as client:
        result = await client.get("/games/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code


@pytest.mark.asyncio
async def test_returns_501_on_get_game(client: TestClient) -> None:
    game = GameFactory()
    async with AsyncClient(app=app, base_url="http://test") as client:
        result = await client.post(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code


@pytest.mark.asyncio
async def test_returns_501_on_delete_game(client: TestClient) -> None:
    game = GameFactory()
    async with AsyncClient(app=app, base_url="http://test") as client:
        result = await client.delete(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code


@pytest.mark.asyncio
async def test_returns_501_on_update_game(client: TestClient) -> None:
    game = GameFactory()
    async with AsyncClient(app=app, base_url="http://test") as client:
        result = await client.put(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code
