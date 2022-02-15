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
from tests.factories import UpdateGameRequestFactory


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
    assert models.Game(**asdict(game)).dict() == result.json()


@pytest.mark.anyio
async def test_returns_200_on_delete_game(
    client: AsyncClient,
    collection: AsyncIOMotorCollection,
) -> None:
    games = GameFactory.build_batch(10)
    game = games[0]
    serialized = [models.Game(**asdict(g)).dict() for g in games]
    await collection.insert_many(serialized)
    result = await client.delete(f"/game/{game.id}/")
    games_in_db = collection.find({})
    expected = [models.Game(**g).dict() async for g in games_in_db]
    actual = [
        models.Game(**asdict(g)).dict() for g in games if g.id != game.id
    ]
    assert HTTPStatus.OK == result.status_code
    assert expected == actual


@pytest.mark.anyio
async def test_returns_200_on_update_game(
    client: AsyncClient,
    collection: AsyncIOMotorCollection,
) -> None:
    game = GameFactory()
    await collection.insert_one(models.Game(**asdict(game)).dict())
    request = UpdateGameRequestFactory()
    params = {k: v for k, v in asdict(request).items() if k != "id"}
    payload = models.GamePayload(**params).dict()
    result = await client.put(f"/game/{game.id}/", json=payload)
    expected_in_db = await collection.find_one({"id": game.id})
    assert HTTPStatus.OK == result.status_code
    assert request.title == expected_in_db["title"]
