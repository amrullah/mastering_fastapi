from sqlalchemy.orm import Session

from db.models import Article
from schemas import ArticleBase


def create_article(db: Session, request: ArticleBase):
    new_article = Article(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id).first()

    return article