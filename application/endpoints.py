from http import HTTPStatus

from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/games/")
async def get_all_games() -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.post("/game/{game_id}/")
async def get_game(game_id: str) -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)


@router.delete("/game/{game_id}/")
async def delete_game(game_id: str) -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)
