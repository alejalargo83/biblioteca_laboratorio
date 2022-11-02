import db
from sqlalchemy import Boolean, Column, Date, Integer, String


class Book(db.Base):
    """Este modelo define los atributos de la tabla book y sus tipos de dato"""
    __tablename__ = "book"
    isbn = Column(Integer, primary_key=True, index=True)
    title = Column("title", String(255))
    description = Column("description", String(255))
    condition = Column("condition", Integer)
    price = Column("price", String(255))
    editorial = Column("editorial", String(255))
    language = Column("language", String(255))
    author = Column("author", String(255))
    number_pages = Column("number_pages", String(255))
    gender = Column("gender", String(255))
    state = Column("state", Boolean, default=False) # True el online y False offline

