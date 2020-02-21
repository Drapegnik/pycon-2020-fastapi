from fastapi import FastAPI

from . import models
from .api import items, users
from .database import engine

app = FastAPI()
app.include_router(users.router, tags=["users"])
app.include_router(items.router, tags=["items"])


@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)
