from factory import Factory
from factory import Faker

from application.controllers import UpdateGameRequest
from application.domain import Game


class GameFactory(Factory):
    class Meta:
        model = Game

    id = Faker("sha1")


class UpdateGameRequestFactory(Factory):
    class Meta:
        model = UpdateGameRequest

    id = Faker("sha1")
