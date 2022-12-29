from typing import Optional

from fastapi import FastAPI, applications
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


class Book(BaseModel):
    id: UUID = Field()
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book", max_length=100, min_length=1)
    rating: int = Field(ge=0, le=100)

    class Config:
        schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "title": "Comp Sci",
                "author": "Coding with Amrullah",
                "description": "Bole to Ekdum jhakaas book hai",
                "rating": 100
            }
        }


BOOKS = []


@app.get("/")
async def read_all_books():
    return BOOKS


@app.post("/")
async def create_book(book: Book) -> Book:
    BOOKS.append(book)
    return book








def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )


applications.get_swagger_ui_html = swagger_monkey_patch