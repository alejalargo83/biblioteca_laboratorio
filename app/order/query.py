import db

# Importamos la tabla order
from .modelo import Order


def get_order_by_id(id: int):
    order = db.session.query(Order).get(id)

    if not order:
        return None

    return order
