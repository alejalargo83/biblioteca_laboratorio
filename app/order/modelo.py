import db
from sqlalchemy import Boolean, Column, Date, Integer, String


class Order(db.Base):
    """Este modelo define los atributos de la tabla order y sus tipos de dato"""
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    detail_order = Column(String(255), foreign_key=True, index=True)
    creation_date = Column("creation_date", Date)
    guide_number = Column("guide_number", String(255))
    shipping_address = Column("shipping_address", String(255))
    send_date = Column("send_date", Date)
    order_status = Column("order_status", String(255))