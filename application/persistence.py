from application.domain import Game


class GameRepository:
    async def get_all(self) -> list[Game]:
        raise NotImplementedError
