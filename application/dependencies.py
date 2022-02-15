from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection

from application.settings import Settings

dependencies = {}


def get_settings() -> Settings:
    return Settings()


def setup_mongo_client() -> None:
    settings = get_settings()
    connection_string = settings.mongo_connection_string
    host = connection_string if connection_string else None
    client = AsyncIOMotorClient(host=host)
    dependencies["mongo_client"] = client


def get_mongo_client() -> AsyncIOMotorClient:
    return dependencies["mongo_client"]


def get_mongo_db_collection(
    settings: Settings = Depends(get_settings),
    client: AsyncIOMotorClient = Depends(get_mongo_client),
) -> AsyncIOMotorCollection:
    db = client[settings.mongo_db]
    return db[settings.mongo_collection]
