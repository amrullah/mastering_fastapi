from typing import List

from pydantic import BaseModel

from db.models import User


class UserArticleSchema(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    items: List[UserArticleSchema] = []

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleUserSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: ArticleUserSchema

    class Config:
        orm_mode = True