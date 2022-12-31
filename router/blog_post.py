from typing import Optional, List, Dict

from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)


class BlogImage(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str]
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[BlogImage] = None


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
                    deprecated=True),
        content: str = Body("Hi how are you"),  # this is a required field, other than the blog object, in the request
        some_more_content: str = Body(..., min_length=10),  # this is optional, due to ... provided for default param
        v: Optional[List[str]] = Query(default=["1.0", "1.1"])  # accepts multi-value query param, v=1&v=2... and so on
    ):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id,
        "content": content,
        'version': v,
        'some_more_content': some_more_content
    }


def required_functionality():
    return {'message': 'Learning FastAPI is important'}
