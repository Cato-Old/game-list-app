from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from application.controllers import AllGamesController

router = APIRouter()


@router.get("/games/")
async def get_all_games(controller: AllGamesController = Depends()) -> None:
    try:
        await controller.get_all()
    except NotImplementedError:
        raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.post("/game/{game_id}/")
async def get_game(game_id: str) -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.delete("/game/{game_id}/")
async def delete_game(game_id: str) -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.put("/game/{game_id}/")
async def update_game(game_id: str) -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)
