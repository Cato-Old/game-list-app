import pytest
from mockito import mock

from application.controllers import AllGamesController
from application.controllers import DeleteGameController
from application.controllers import GetGameController
from application.controllers import UpdateGameController
from application.domain import GameId
from application.persistence import GameRepository
from tests.factories import UpdateGameRequestFactory


@pytest.fixture
def repository() -> GameRepository:
    return mock(GameRepository)


@pytest.mark.asyncio
async def test_all_games_controller_raises_on_get_all(
    repository: GameRepository,
) -> None:
    controller = AllGamesController(repository=repository)
    with pytest.raises(NotImplementedError):
        await controller.get_all()


@pytest.mark.asyncio
async def test_get_game_controller_raises_on_get(
    repository: GameRepository,
) -> None:
    controller = GetGameController(repository=repository)
    game_id = GameId("foo")
    with pytest.raises(NotImplementedError):
        await controller.get(game_id)


@pytest.mark.asyncio
async def test_delete_game_controller_raises_on_delete(
    repository: GameRepository,
) -> None:
    controller = DeleteGameController(repository=repository)
    game_id = GameId("foo")
    with pytest.raises(NotImplementedError):
        await controller.delete(game_id)


@pytest.mark.asyncio
async def test_update_game_controller_raises_on_update(
    repository: GameRepository,
) -> None:
    controller = UpdateGameController(repository=repository)
    request = UpdateGameRequestFactory()
    with pytest.raises(NotImplementedError):
        await controller.update(request=request)
