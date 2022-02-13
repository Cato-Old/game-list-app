from dataclasses import dataclass

from application.domain import Game
from application.domain import GameId


@dataclass
class UpdateGameRequest:
    id: GameId


class AllGamesController:
    async def get_all(self) -> list[Game]:
        raise NotImplementedError


class GetGameController:
    async def get(self, game_id: GameId) -> Game:
        raise NotImplementedError


class DeleteGameController:
    async def delete(self, game_id: GameId) -> None:
        raise NotImplementedError


class UpdateGameController:
    async def update(self, request: UpdateGameRequest) -> None:
        raise NotImplementedError
