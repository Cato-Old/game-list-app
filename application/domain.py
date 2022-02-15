from dataclasses import dataclass
from dataclasses import dataclass
from typing import NewType

GameId = NewType("GameId", str)


@dataclass(frozen=True)
class Game:
    id: GameId
    title: str


@dataclass(frozen=True)
class UpdateGameRequest:
    id: GameId
    title: str
