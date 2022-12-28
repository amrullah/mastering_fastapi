from fastapi import FastAPI, applications
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
async def first_api():
    return {"message": "Hello Amrullah"}


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )
applications.get_swagger_ui_html = swagger_monkey_patch