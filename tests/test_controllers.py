import pytest

from application.controllers import AllGamesController
from application.controllers import DeleteGameController
from application.controllers import GetGameController
from application.domain import GameId


@pytest.mark.asyncio
async def test_all_games_controller_raises_on_get_all() -> None:
    controller = AllGamesController()
    with pytest.raises(NotImplementedError):
        await controller.get_all()


@pytest.mark.asyncio
async def test_get_game_controller_raises_on_get() -> None:
    controller = GetGameController()
    game_id = GameId("foo")
    with pytest.raises(NotImplementedError):
        await controller.get(game_id)


@pytest.mark.asyncio
async def test_delete_game_controller_raises_on_delete() -> None:
    controller = DeleteGameController()
    game_id = GameId("foo")
    with pytest.raises(NotImplementedError):
        await controller.delete(game_id)
