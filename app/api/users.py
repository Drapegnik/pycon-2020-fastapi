from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, deps, schemas

router = APIRouter()


@router.get("/users", response_model=List[schemas.User])
def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    return crud.get_users(db, skip=skip, limit=limit)


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already in use")
    return crud.create_user(db, user)


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(deps.get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
