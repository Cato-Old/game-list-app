from dataclasses import dataclass
from typing import NewType

GameId = NewType("GameId", str)


@dataclass(frozen=True)
class Game:
    id: GameId
