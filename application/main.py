from fastapi import FastAPI

from application import endpoints

app = FastAPI()

app.include_router(endpoints.router)
