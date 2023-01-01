from fastapi import FastAPI, applications
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine
from router import blog_get, blog_post, user, article

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )


applications.get_swagger_ui_html = swagger_monkey_patch


models.Base.metadata.create_all(engine)
# --------------------------------------------------------
