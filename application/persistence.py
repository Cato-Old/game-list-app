from dataclasses import asdict

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
        result = await self._collection.find_one({"id": game_id})
        model = models.Game.parse_obj(result)
        return Game(**model.dict())

    async def delete(self, game_id: GameId) -> None:
        await self._collection.delete_one({"id": game_id})

    async def update(self, request: UpdateGameRequest) -> None:
        fields = {k: v for k, v in asdict(request).items() if k != "id"}
        update_query = {"$set": {k: v} for k, v in fields.items() if v}
        await self._collection.find_one_and_update(
            {"id": request.id},
            update_query
        )
