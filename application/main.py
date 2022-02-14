from fastapi import FastAPI

from application import endpoints
from application.dependencies import setup_mongo_client

app = FastAPI()

app.include_router(endpoints.router)
app.add_event_handler("startup", setup_mongo_client)
