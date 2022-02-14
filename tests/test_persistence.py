import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection

from application.dependencies import get_mongo_client
from application.dependencies import setup_mongo_client
from application.domain import GameId
from application.persistence import GameRepository
from application.settings import Settings
from tests.factories import UpdateGameRequestFactory


@pytest.fixture
async def collection(settings: Settings) -> AsyncIOMotorCollection:
    setup_mongo_client()
    client = get_mongo_client()
    db = client[settings.mongo_db]
    return db[settings.mongo_collection]


@pytest.fixture
def repository(collection: AsyncIOMotorCollection) -> GameRepository:
    return GameRepository(collection=collection)


@pytest.mark.anyio
async def test_raises_on_get_all(repository: GameRepository) -> None:
    with pytest.raises(NotImplementedError):
        await repository.get_all()


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
