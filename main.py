from enum import Enum
from typing import Optional

from fastapi import FastAPI, applications, status, Response
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )


applications.get_swagger_ui_html = swagger_monkey_patch


# --------------------------------------------------------
@app.get(
    '/blogs/all',
    tags=['blog'],
    summary="Retrieve all blogs",
    description="Simulates List blogs api",
    response_description="List of all blogs"
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}


@app.get(
    '/blog/{id}/comments/{comment_id}',
    tags=['blog', 'comment']
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


@app.get("/blog/type/{type}", tags=['blog'])
def get_blog_type(blog_type: BlogType):
    return {'message': f'Blog type {blog_type}'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}

    return {'message': f'Blog with id {id}'}