import asyncio
import os

from motor.motor_asyncio import AsyncIOMotorClient
from pytest import fixture

from application.dependencies import dependencies
from application.settings import Settings
from tests.settings import SETTINGS


@fixture(autouse=True)
def load_settings() -> None:
    for k, v in SETTINGS.items():
        if k not in os.environ:
            os.environ[k] = v


@fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@fixture
def settings() -> Settings:
    return Settings()


@fixture
def motor_client() -> AsyncIOMotorClient:
    return dependencies["mongo_client"]
