from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from application import models
from application.dependencies import get_mongo_db_collection
from application.domain import UpdateGameRequest
from application.domain import Game
from application.domain import GameId


class GameRepository:
    def __init__(
        self,
        collection: AsyncIOMotorCollection = Depends(get_mongo_db_collection),
    ) -> None:
        self._collection = collection

    async def get_all(self) -> list[Game]:
        cursor = self._collection.find({})
        game_models = [models.Game(**i) async for i in cursor]
        return [Game(**m.dict()) for m in game_models]

    async def get_one(self, game_id: GameId) -> Game:
        raise NotImplementedError

    async def delete(self, game_id: GameId) -> None:
        raise NotImplementedError

    async def update(self, request: UpdateGameRequest) -> None:
        raise NotImplementedError
