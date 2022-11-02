import db
from sqlalchemy import Column, Date, Integer, String


class Card(db.Base):
    """Este modelo define los atributos de la tabla card y sus tipos de dato"""
    __tablename__ = "card"
    number = Column(Integer, primary_key=True, index=True)
    name_card = Column("name_card", String(255))
    code = Column("code", String(255))
    expiration_date = Column("expiration_date", Date)
