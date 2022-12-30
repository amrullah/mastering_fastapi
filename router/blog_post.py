from typing import Optional

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post("/new/{id}")
def create_post(blog: BlogModel, id: int, version: int = 1):
    # blog is request body, id is path parameter and version is query parameter
    return "OK"
