from fastapi import APIRouter

from .query import get_user_by_dni

router = APIRouter()

# Ruta para obtener 1 cliente
@router.get("/{dni}")
def get_user(dni: int):
    user = get_user_by_dni(dni=dni)

    if not user:
        return {}

    return {
        "dni": user.dni
    }
