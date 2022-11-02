import db

# Importamos la tabla book
from .modelo import Book


def get_book_by_isbn(isbn: int):
    book = db.session.query(book).get(isbn)

    if not book:
        return None

    return book
