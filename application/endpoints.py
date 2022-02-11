from http import HTTPStatus

from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/games/")
async def get_all_games() -> None:
    raise HTTPException(status_code=HTTPStatus.NOT_IMPLEMENTED)
