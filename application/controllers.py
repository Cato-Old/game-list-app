from fastapi import Depends

from application.domain import Game
from application.domain import GameId
from application.domain import UpdateGameRequest
from application.persistence import GameRepository


class AllGamesController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        self._repo = repository

    async def get_all(self) -> list[Game]:
        raise NotImplementedError


class GetGameController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        self._repo = repository

    async def get(self, game_id: GameId) -> Game:
        raise NotImplementedError


class DeleteGameController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        pass

    async def delete(self, game_id: GameId) -> None:
        raise NotImplementedError


class UpdateGameController:
    def __init__(self, repository: GameRepository = Depends()) -> None:
        pass

    async def update(self, request: UpdateGameRequest) -> None:
        raise NotImplementedError
