import db
from sqlalchemy import Boolean, Column, Date, Integer, String


class Gender(db.Base):
    """Este modelo define los atributos de la tabla gender y sus tipos de dato"""
    __tablename__ = "gender"
    id = Column(Integer, primary_key=True, index=True)
    name = Column("name", String(255))
