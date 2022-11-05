import db
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Aquí hay un relación de 1 a muchos
# User.type * ---> 1 user_type
# Un usuario tiene 1 tipo, pero un 1 tipo lo pueden tener muchos usuarios
# Ejemplo de ayuda https://programmerclick.com/article/9595776150

class UserType(db.Base):
    """Este modelo define los atributos de la tabla user_type y sus tipos de dato"""
    __tablename__ = "user_type"
    id = Column(Integer, primary_key=True, index=True)
    rol = Column("role", Integer)
    user = relationship("User", back_populates = "users")

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
    news = Column("news", Boolean, default=False)
    state = Column("state", Boolean, default=False) # True el online y False offline
    type = Column(Integer, ForeignKey(UserType.id))
