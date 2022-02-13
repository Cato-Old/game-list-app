import pytest

from application.controllers import AllGamesController


@pytest.mark.asyncio
async def test_all_games_controller_raises_on_get_all() -> None:
    controller = AllGamesController()
    with pytest.raises(NotImplementedError):
        await controller.get_all()
