from typing import List

from fastapi import APIRouter
from .models import executor, oredeer, User, client
from .resolvers import add_new_group, get_group, get_groups, update_group, delete_current_group

router = APIRouter()


@router.get('/')
def get_client() -> List[client]:
    return get_client()


@router.get('/{client_id}')
def get_current_client(client_id: int) -> client:
    return get_client(client_id)


@router.post('/')f
def add_group(new_group: ImputGroup) -> NewId:
    return add_new_group(new_group)


@router.put('/{group_id}')
def add_group(group_id: int, new_group: ImputGroup) -> NewId:
    return update_group(group_id, new_group)


@router.delete("/{group_id}")
def delete_group(group_id: int) -> NewId:
    return delete_current_group(group_id)