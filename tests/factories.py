from factory import Factory
from factory import Faker
from factory.fuzzy import FuzzyText

from application.domain import UpdateGameRequest
from application.domain import Game


class GameFactory(Factory):
    class Meta:
        model = Game

    id = Faker("sha1")
    title = FuzzyText()


class UpdateGameRequestFactory(Factory):
    class Meta:
        model = UpdateGameRequest

    id = Faker("sha1")
    title = FuzzyText()
