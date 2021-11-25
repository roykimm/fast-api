from fastapi import APIRouter
from enum import Enum

router = APIRouter(
    prefix="/book",
    tags=['Books'],
)

BOOKS = {
    'book_1': {'title': 'Title one', 'author': 'roykimm'},
    'book_2': {'title': 'Title two', 'author': 'daldog'},
    'book_3': {'title': 'Title three', 'author': 'gobella'},
    'book_4': {'title': 'Title four', 'author': 'goroy'},
    'book_5': {'title': 'Title five', 'author': 'ej'},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@router.get('/')
async def read_all_books():
    return BOOKS


@router.get('/{book_name}')
async def read_book(book_name: str):
    return BOOKS[book_name]


@router.get('/mybook')
async def read_favorite_book():
    return {"book_title": "my favorite book"}


@router.get('/{book_id}')
async def read_book(book_id: int):
    return {"book_title": book_id}


@router.get('/directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"diection": direction_name, "sub": "Up"}
    elif direction_name == DirectionName.south:
        return {"diection": direction_name, "sub": "Up"}
    elif direction_name == DirectionName.east:
        return {"diection": direction_name, "sub": "Up"}
    elif direction_name == DirectionName.west:
        return {"diection": direction_name, "sub": "Up"}
