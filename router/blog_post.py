from fastapi import APIRouter
from starlette import status
from starlette.responses import Response


router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

@router.post("/new")
def create_post():
    pass