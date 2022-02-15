from dataclasses import asdict
from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from application import models
from application.controllers import AllGamesController
from application.controllers import DeleteGameController
from application.controllers import GetGameController
from application.controllers import UpdateGameController
from application.domain import UpdateGameRequest
from application.domain import GameId

router = APIRouter()


@router.get("/games/")
async def get_all_games(
    controller: AllGamesController = Depends(),
) -> list[models.Game]:
    games = await controller.get_all()
    return [models.Game(**asdict(g)) for g in games]


@router.post("/game/{game_id}/")
async def get_game(
    game_id: str,
    controller: GetGameController = Depends(),
) -> models.Game:
    game = await controller.get(GameId(game_id))
    return models.Game(**asdict(game))


@router.delete("/game/{game_id}/")
async def delete_game(
    game_id: str,
    controller: DeleteGameController = Depends(),
) -> None:
    await controller.delete(GameId(game_id))


@router.put("/game/{game_id}/")
async def update_game(
    game_id: str,
    controller: UpdateGameController = Depends(),
) -> None:
    request = UpdateGameRequest(id=GameId(game_id))
    try:
        await controller.update(request)
    except NotImplementedError:
        raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)
