import db

# Importamos la tabla gender
from .modelo import Gender


def get_gender_by_id(id: int):
    gender = db.session.query(Gender).get(id)

    if not gender:
        return None

    return gender
