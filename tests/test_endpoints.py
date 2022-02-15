from dataclasses import asdict
from http import HTTPStatus

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection

from application import models
from application.dependencies import get_mongo_db_collection
from application.main import app
from application.settings import Settings
from tests.factories import GameFactory


@pytest.fixture
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        async with LifespanManager(app):
            yield client


@pytest.fixture
async def collection(
    settings: Settings,
    motor_client: AsyncIOMotorClient,
) -> AsyncIOMotorCollection:
    collection = get_mongo_db_collection(settings, motor_client)
    yield collection
    await collection.drop()


@pytest.mark.anyio
async def test_returns_200_on_get_all_games(
    client: AsyncClient,
    collection: AsyncIOMotorCollection,
) -> None:
    games = GameFactory.build_batch(10)
    serialized = [models.Game(**asdict(g)).dict() for g in games]
    await collection.insert_many(serialized)
    result = await client.get("/games/")
    assert HTTPStatus.OK == result.status_code
    assert [models.Game(**asdict(g)).dict() for g in games] == result.json()


@pytest.mark.anyio
async def test_returns_200_on_get_game(
    client: AsyncClient,
    collection: AsyncIOMotorCollection,
) -> None:
    game = GameFactory()
    await collection.insert_one(models.Game(**asdict(game)).dict())
    result = await client.post(f"/game/{game.id}/")
    assert HTTPStatus.OK == result.status_code


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
