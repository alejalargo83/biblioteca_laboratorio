from fastapi import APIRouter, HTTPException

from .modelo import Card
from .query import get_card_by_number

router = APIRouter()

# Ruta para obtener 1 tarjeta
@router.get("/{number}")
def get_card(number: int):
    card: Card = get_card_by_number(number=number)

    if not card:
        raise HTTPException(status_code=404, detail="card not found")

    return {
        "number": card.number,
        "name_card": card.name_card,
        "code": card.code,
        "expiration_date": card.expiration_date,
    }
