from dataclasses import asdict
from typing import Generator

import pytest
from motor.motor_asyncio import AsyncIOMotorCollection

from application.dependencies import get_mongo_client
from application.dependencies import setup_mongo_client
from application.domain import GameId
from application import models
from application.persistence import GameRepository
from application.settings import Settings
from tests.factories import GameFactory
from tests.factories import UpdateGameRequestFactory


@pytest.fixture
async def collection(
    settings: Settings,
) -> Generator[AsyncIOMotorCollection, None, None]:
    setup_mongo_client()
    client = get_mongo_client()
    db = client[settings.mongo_db]
    collection = db[settings.mongo_collection]
    yield collection
    await collection.drop()


@pytest.fixture
def repository(collection: AsyncIOMotorCollection) -> GameRepository:
    return GameRepository(collection=collection)


@pytest.mark.anyio
async def test_returns_all_games_on_get_all(
    repository: GameRepository,
    collection: AsyncIOMotorCollection,
) -> None:
    expected = GameFactory.build_batch(10)
    games = [models.Game(**asdict(g)) for g in expected]
    await collection.insert_many(m.dict() for m in games)
    actual = await repository.get_all()
    assert sorted(expected, key=lambda g: g.id) == sorted(actual, key=lambda g: g.id)


@pytest.mark.anyio
async def test_raises_on_get_one(repository: GameRepository) -> None:
    game_id = GameId("foo")
    with pytest.raises(NotImplementedError):
        await repository.get_one(game_id)


@pytest.mark.anyio
async def test_raises_on_delete(repository: GameRepository) -> None:
    game_id = GameId("bar")
    with pytest.raises(NotImplementedError):
        await repository.delete(game_id)


@pytest.mark.anyio
async def test_raises_on_update(repository: GameRepository) -> None:
    request = UpdateGameRequestFactory()
    with pytest.raises(NotImplementedError):
        await repository.update(request)
