from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from application.dependencies import get_mongo_db_collection
from application.domain import UpdateGameRequest
from application.domain import Game
from application.domain import GameId


class GameRepository:
    def __init__(
        self,
        collection: AsyncIOMotorCollection = Depends(get_mongo_db_collection),
    ) -> None:
        pass

    async def get_all(self) -> list[Game]:
        raise NotImplementedError

    async def get_one(self, game_id: GameId) -> Game:
        raise NotImplementedError

    async def delete(self, game_id: GameId) -> None:
        raise NotImplementedError

    async def update(self, request: UpdateGameRequest) -> None:
        raise NotImplementedError
