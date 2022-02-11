from factory import Factory
from factory import Faker

from application.domain import Game


class GameFactory(Factory):
    class Meta:
        model = Game

    id = Faker("sha1")
