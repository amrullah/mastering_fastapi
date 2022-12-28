from fastapi import FastAPI, applications
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

BOOKS = {
    'book1': {'title': 'Title One', 'author': 'Author One'},
    'book2': {'title': 'Title Two', 'author': 'Author Two'},
    'book3': {'title': 'Title Three', 'author': 'Author Three'},
    'book4': {'title': 'Title Four', 'author': 'Author Four'},
    'book5': {'title': 'Title Five', 'author': 'Author Five'},

}


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")  # keep it above "/books/{book_id}" path, else "/books/{book_id}" will override this path
async def read_favorite_book():
    return BOOKS["book2"]


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return BOOKS[f"book{book_id}"]


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )


applications.get_swagger_ui_html = swagger_monkey_patch
