from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_connection_string: str
    mongo_db: str
    mongo_collection: str
