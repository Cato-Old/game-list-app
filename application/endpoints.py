from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from application.controllers import AllGamesController
from application.controllers import DeleteGameController
from application.controllers import GetGameController
from application.controllers import UpdateGameController
from application.domain import UpdateGameRequest
from application.domain import GameId

router = APIRouter()


@router.get("/games/")
async def get_all_games(controller: AllGamesController = Depends()) -> None:
    try:
        await controller.get_all()
    except NotImplementedError:
        raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.post("/game/{game_id}/")
async def get_game(
    game_id: str,
    controller: GetGameController = Depends(),
) -> None:
    try:
        await controller.get(GameId(game_id))
    except NotImplementedError:
        raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.delete("/game/{game_id}/")
async def delete_game(
    game_id: str,
    controller: DeleteGameController = Depends(),
) -> None:
    try:
        await controller.delete(GameId(game_id))
    except NotImplementedError:
        raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


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
