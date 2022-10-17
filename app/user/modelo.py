import db
from sqlalchemy import Boolean, Column, Date, Integer, String


class User(db.Base):
    """Este modelo define los atributos de la tabla user y sus tipos de dato"""
    __tablename__ = "user"
    dni = Column(Integer, primary_key=True, index=True)
    name = Column("name", String(255))
    last_name = Column("last_name", String(255))
    password = Column("password", String(255))
    email = Column("email", String(255))
    addres = Column("addres", String(255))
    birth_date = Column("birth_date", Date)
    type = Column("type", Integer)
    news = Column("news", Boolean, default=False)
    state = Column("state", Boolean, default=False) # True el online y False offline

