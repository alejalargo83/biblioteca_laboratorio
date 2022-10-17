from fastapi import APIRouter, HTTPException

from .modelo import User
from .query import get_user_by_dni

router = APIRouter()

# Ruta para obtener 1 cliente
@router.get("/{dni}")
def get_user(dni: int):
    user: User = get_user_by_dni(dni=dni)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    return {
        "dni": user.dni,
        "name": user.name,
        "last_name": user.last_name,
    }
