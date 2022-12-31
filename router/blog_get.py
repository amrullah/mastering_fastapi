from enum import Enum
from typing import Optional

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response

from .blog_post import required_functionality

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)


@router.get(
    '/all',
    summary="Retrieve all blogs",
    description="Simulates List blogs api",
    response_description="List of all blogs"
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None,
                  req_parameters: dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}',
            'req': req_parameters}


@router.get(
    '/{id}/comments/{comment_id}',
    tags=['comment']
)
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory
    - **comment_id** mandatory
    """
    return {'message': f'blog_id {id} comment_id {comment_id}, valid {valid} username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    how_to = 'howto'


@router.get("/type/{type}")
def get_blog_type(blog_type: BlogType):
    return {'message': f'Blog type {blog_type}'}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response, req_parameters: dict = Depends(required_functionality)):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}

    return {'message': f'Blog with id {id}',
            'req': req_parameters}
