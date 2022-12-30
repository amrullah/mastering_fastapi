from typing import Optional

from fastapi import APIRouter, Query
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


@router.post("/new/{id}/comment")
def create_comment(
        blog: BlogModel, id: int, comment_id:
        int = Query(title="Id of the comment",
                    description="Some description for comment_id",
                    alias="commentId",  # this will be the json field key
                    deprecated=True)):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id
    }