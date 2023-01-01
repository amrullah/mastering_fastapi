from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter(
    prefix='/article',
    tags=['article']
)


@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request=request)


@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)
