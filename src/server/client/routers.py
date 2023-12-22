from typing import List

from fastapi import APIRouter
from .models import ImputClient, OutputClient, NewId
from .resolvers import add_new_client, get_clients, get_client, update_client, delete_current_client


router = APIRouter()


@router.get('/')
def get_client() -> List[OutputClient]:
    return get_clients()


@router.get('/{client_id}')
def get_current_client(client_id: int) -> OutputClient:
    return get_client(client_id)


@router.post('/')
def add_client(new_client: ImputClient) -> NewId:
    return add_new_client(new_client)


@router.put('/{client_id}')
def add_client(client_id: int, new_client: ImputClient) -> NewId:
    return update_client(client_id, new_client)


@router.delete("/{client_id}")
def delete_client(client_id: int) -> NewId:
    return delete_current_client(client_id)