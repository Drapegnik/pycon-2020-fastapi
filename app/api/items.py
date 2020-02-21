from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, deps, schemas

router = APIRouter()


@router.get("/items", response_model=List[schemas.Item])
def read_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    return crud.get_items(db, skip=skip, limit=limit)


@router.post("/users/{user_id}/items", response_model=schemas.Item)
def create_item(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(deps.get_db)
):
    return crud.create_user_item(db, item, user_id)
