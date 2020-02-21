from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models
from .database import SessionLocal, engine

app = FastAPI()


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User).first()


@app.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = f"kek {user.password}"
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)
