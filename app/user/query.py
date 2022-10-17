import db

# Importamos la tabla user
from .modelo import User


def get_user_by_dni(dni: int):
    user = db.session.query(User).get(dni)

    if not user:
        return None

    return user
