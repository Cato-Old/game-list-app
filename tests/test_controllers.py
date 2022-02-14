from asyncio import Future

import pytest
from mockito import mock
from mockito import when

from application.controllers import AllGamesController
from application.controllers import DeleteGameController
from application.controllers import GetGameController
from application.controllers import UpdateGameController
from application.domain import Game
from application.domain import GameId
from application.persistence import GameRepository
from tests.factories import GameFactory
from tests.factories import UpdateGameRequestFactory


@pytest.fixture
def repository() -> GameRepository:
    return mock(GameRepository)


def setup_get_all(repository: GameRepository, expected: list[Game]) -> None:
    coroutine = Future()
    coroutine.set_result(expected)
    when(repository).get_all().thenReturn(coroutine)


def setup_get_one(repository: GameRepository, expected: Game) -> None:
    coroutine = Future()
    coroutine.set_result(expected)
    when(repository).get_one(expected.id).thenReturn(coroutine)


@pytest.mark.asyncio
async def test_all_games_controller_raises_on_get_all(
    repository: GameRepository,
) -> None:
    expected = GameFactory.build_batch(5)
    setup_get_all(repository, expected)
    controller = AllGamesController(repository=repository)
    actual = await controller.get_all()
    assert expected == actual


@pytest.mark.asyncio
async def test_get_game_controller_raises_on_get(
    repository: GameRepository,
) -> None:
    expected = GameFactory()
    setup_get_one(repository, expected)
    controller = GetGameController(repository=repository)
    actual = await controller.get(expected.id)
    assert expected == actual


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
