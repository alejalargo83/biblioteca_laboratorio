import db

# Importamos la tabla card
from .modelo import Card


def get_card_by_number(number: int):
    card = db.session.query(Card).get(number)

    if not card:
        return None

    return card
