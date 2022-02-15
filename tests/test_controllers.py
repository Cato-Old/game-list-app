from asyncio import Future

import pytest
from mockito import mock
from mockito import verify
from mockito import when

from application.controllers import AllGamesController
from application.controllers import DeleteGameController
from application.controllers import GetGameController
from application.controllers import UpdateGameController
from application.domain import Game
from application.domain import UpdateGameRequest
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


def setup_delete(repository: GameRepository, game: Game) -> None:
    coroutine = Future()
    coroutine.set_result(None)
    when(repository).delete(game.id).thenReturn(coroutine)


def setup_update(repository: GameRepository, req: UpdateGameRequest) -> None:
    coroutine = Future()
    coroutine.set_result(None)
    when(repository).update(req).thenReturn(coroutine)


@pytest.mark.anyio
async def test_all_games_controller_returns_on_get_all(
    repository: GameRepository,
) -> None:
    expected = GameFactory.build_batch(5)
    setup_get_all(repository, expected)
    controller = AllGamesController(repository=repository)
    actual = await controller.get_all()
    assert expected == actual


@pytest.mark.anyio
async def test_get_game_controller_returns_on_get(
    repository: GameRepository,
) -> None:
    expected = GameFactory()
    setup_get_one(repository, expected)
    controller = GetGameController(repository=repository)
    actual = await controller.get(expected.id)
    assert expected == actual


@pytest.mark.anyio
async def test_delete_game_controller_deletes_on_delete(
    repository: GameRepository,
) -> None:
    expected = GameFactory()
    setup_delete(repository, expected)
    controller = DeleteGameController(repository=repository)
    await controller.delete(expected.id)
    verify(repository).delete(...)


@pytest.mark.anyio
async def test_update_game_controller_updates_on_update(
    repository: GameRepository,
) -> None:
    request = UpdateGameRequestFactory()
    setup_update(repository, request)
    controller = UpdateGameController(repository=repository)
    await controller.update(request=request)
    verify(repository).update(...)
