from typing import List

from fastapi import APIRouter
from .models import ImputOrders, OutputOrders, NewId
from .resolvers import get_orders, add_new_orders, update_orders, delete_current_orders


router = APIRouter()


@router.get('/')
def get_orders() -> List[OutputOrders]:
    return get_orders()


@router.get('/{orders_id}')
def get_current_orders(orders_id: int) -> OutputOrders:
    return get_orders(orders_id)


@router.post('/')
def add_orders(new_orders: ImputOrders) -> NewId:
    return add_new_orders(new_orders)


@router.put('/{orders_id}')
def add_orders(orders_id: int, new_orders: ImputOrders) -> NewId:
    return update_orders(orders_id, new_orders)


@router.delete("/{orders_id}")
def delete_orders(orders_id: int) -> NewId:
    return delete_current_orders(orders_id)