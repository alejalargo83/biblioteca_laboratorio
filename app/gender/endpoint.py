from fastapi import APIRouter, HTTPException

from .modelo import Gender
from .query import get_gender_by_id

router = APIRouter()

# Ruta para obtener 1 genero
@router.get("/{id}")
def get_gender(id: int):
    gender: Gender = get_gender_by_id(id=id)

    if not gender:
        raise HTTPException(status_code=404, detail="gender not found")

    return {
        "id": gender.id,
        "name": gender.name
    }
