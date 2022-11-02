from fastapi import APIRouter, HTTPException

from .modelo import Order
from .query import get_order_by_id

router = APIRouter()

# Ruta para obtener 1 orden
@router.get("/{id}")
def get_order(id: int):
    order: Order = get_order_by_id(id=id)

    if not order:
        raise HTTPException(status_code=404, detail="order not found")

    return {
        "id": order.id,
        "detail_order": order.detail_order,
        "creation_date": order.creation_date,
        "guide_number": order.guide_number,
        "shipping_address": order.shipping_address,
        "send_date": order.send_date,
        "order_status": order.order_status
    }
