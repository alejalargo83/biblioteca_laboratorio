from fastapi import APIRouter, HTTPException

from .modelo import Book
from .query import get_book_by_isbn

router = APIRouter()

# Ruta para obtener 1 libro
@router.get("/{isbn}")
def get_book(isbn: int):
    book: Book = get_book_by_isbn(isbn=isbn)

    if not book:
        raise HTTPException(status_code=404, detail="book not found")

    return {
        "isbn": book.isbn,
        "title": book.title,
        "description": book.description,
        "condition": book.condition,
        "price": book.price,
        "editorial": book.editorial,
        "language": book.language,
        "author": book.author,
        "number_pages": book.number_pages,
        "gender": book.gender,
        "state": book.state
    }
