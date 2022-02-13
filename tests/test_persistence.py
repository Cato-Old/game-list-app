import pytest

from application.persistence import GameRepository


@pytest.fixture
def repository() -> GameRepository:
    return GameRepository()


@pytest.mark.asyncio
async def test_raises_on_get_all(repository: GameRepository) -> None:
    with pytest.raises(NotImplementedError):
        await repository.get_all()
