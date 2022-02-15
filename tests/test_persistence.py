from dataclasses import asdict
from typing import Generator

import pytest
from motor.motor_asyncio import AsyncIOMotorCollection

from application.dependencies import get_mongo_client
from application.dependencies import setup_mongo_client
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
async def test_returns_game_on_get_one(
    repository: GameRepository,
    collection: AsyncIOMotorCollection,
) -> None:
    expected = GameFactory()
    game = models.Game(**asdict(expected))
    await collection.insert_one(game.dict())
    actual = await repository.get_one(expected.id)
    assert expected == actual


@pytest.mark.anyio
async def test_deletes_game_on_delete(
    repository: GameRepository,
    collection: AsyncIOMotorCollection,
) -> None:
    games = GameFactory.build_batch(10)
    game_models = [models.Game(**asdict(g)) for g in games]
    await collection.insert_many(m.dict() for m in game_models)
    game_to_delete = games[0]
    await repository.delete(game_to_delete.id)
    expected = [
        models.Game(**asdict(g)) for g in games if g.id != game_to_delete.id
    ]
    actual = collection.find({})
    assert expected == [models.Game(**g) async for g in actual]


@pytest.mark.anyio
async def test_update_game_on_update(
    repository: GameRepository,
    collection: AsyncIOMotorCollection,
) -> None:
    game = GameFactory()
    request = UpdateGameRequestFactory(id=game.id)
    await collection.insert_one(models.Game(**asdict(game)).dict())
    await repository.update(request)
    expected = await collection.find_one({"id": game.id})
    assert request.title == expected["title"]
