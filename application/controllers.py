from application.domain import Game


class AllGamesController:
    async def get_all(self) -> list[Game]:
        raise NotImplementedError
