import os

from pytest import fixture

from tests.settings import SETTINGS

pytest_plugins = ("pytest_asyncio", )


@fixture(autouse=True)
def load_settings() -> None:
    for k, v in SETTINGS.items():
        if k not in os.environ:
            os.environ[k] = v
