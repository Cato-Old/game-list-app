from fastapi import Depends

from application.domain import Game
from application.domain import GameId
from application.domain import UpdateGameRequest
from application.persistence import GameRepository


class AllGamesController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        self._repo = repository

    async def get_all(self) -> list[Game]:
        return await self._repo.get_all()


class GetGameController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        self._repo = repository

    async def get(self, game_id: GameId) -> Game:
        return await self._repo.get_one(game_id)


class DeleteGameController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        self._repo = repository

    async def delete(self, game_id: GameId) -> None:
        await self._repo.delete(game_id)


class UpdateGameController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        pass

    async def update(self, request: UpdateGameRequest) -> None:
        raise NotImplementedError
