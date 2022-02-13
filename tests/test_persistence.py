import pytest

from application.domain import GameId
from application.persistence import GameRepository
from tests.factories import UpdateGameRequestFactory


@pytest.fixture
def repository() -> GameRepository:
    return GameRepository()


@pytest.mark.asyncio
async def test_raises_on_get_all(repository: GameRepository) -> None:
    with pytest.raises(NotImplementedError):
        await repository.get_all()


@pytest.mark.asyncio
async def test_raises_on_get_one(repository: GameRepository) -> None:
    game_id = GameId("foo")
    with pytest.raises(NotImplementedError):
        await repository.get_one(game_id)


@pytest.mark.asyncio
async def test_raises_on_delete(repository: GameRepository) -> None:
    game_id = GameId("bar")
    with pytest.raises(NotImplementedError):
        await repository.delete(game_id)


@pytest.mark.asyncio
async def test_raises_on_update(repository: GameRepository) -> None:
    request = UpdateGameRequestFactory()
    with pytest.raises(NotImplementedError):
        await repository.update(request)
