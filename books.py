from enum import Enum
from typing import Optional

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


# parameters with no corresponding path variable will be considered query string variables, ie. /?skip_book=...
@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    # you can also provide a default value for the parameter other than None
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/books/mybook")  # keep it above "/books/{book_id}" path, else "/books/{book_id}" will override this path
async def read_favorite_book():
    return BOOKS["book2"]


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return BOOKS[f"book{book_id}"]


class Directions(str, Enum):
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"


@app.get("/directions/{direction}")
async def get_direction(direction: Directions):
    if direction == Directions.NORTH:
        return {"direction": direction, "sub": "Up"}
    if direction == Directions.SOUTH:
        return {"direction": direction, "sub": "Down"}
    if direction == Directions.EAST:
        return {"direction": direction, "sub": "Right"}
    if direction == Directions.WEST:
        return {"direction": direction, "sub": "Left"}


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )


applications.get_swagger_ui_html = swagger_monkey_patch
