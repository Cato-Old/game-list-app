from typing import Optional

from pydantic import BaseModel


class Game(BaseModel):
    id: str
    title: str


class GamePayload(BaseModel):
    title: Optional[str]
