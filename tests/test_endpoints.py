from http import HTTPStatus

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from application.main import app
from tests.factories import GameFactory


@pytest.fixture
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        async with LifespanManager(app):
            yield client


@pytest.mark.anyio
async def test_returns_200_on_get_all_games(client: AsyncClient) -> None:
    result = await client.get("/games/")
    assert HTTPStatus.OK == result.status_code


@pytest.mark.anyio
async def test_returns_501_on_get_game(client: AsyncClient) -> None:
    game = GameFactory()
    result = await client.post(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code


@pytest.mark.anyio
async def test_returns_501_on_delete_game(client: AsyncClient) -> None:
    game = GameFactory()
    result = await client.delete(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code


@pytest.mark.anyio
async def test_returns_501_on_update_game(client: AsyncClient) -> None:
    game = GameFactory()
    result = await client.put(f"/game/{game.id}/")
    assert HTTPStatus.NOT_IMPLEMENTED == result.status_code
