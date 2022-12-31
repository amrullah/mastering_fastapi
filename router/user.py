from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserDisplay)
def create_user(user_request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request=user_request)


