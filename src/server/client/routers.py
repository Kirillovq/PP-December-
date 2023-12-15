from typing import List

from fastapi import APIRouter
from .models import Imputclient, Outputclient, Newclient
from .resolvers import get_clients
#get_client, add_new_client, update_client, delete_current_client


router = APIRouter()


@router.get('/')
def get_client() -> List[Outputclient]:
    return get_clients()


@router.get('/{client_id}')
def get_current_client(client_id: int) -> Outputclient:
    return get_client(client_id)


@router.post('/')
def add_client(new_client: Imputclient) -> Newclient:
    return add_new_client(new_client)


@router.put('/{client_id}')
def add_client(client_id: int, new_client: Imputclient) -> Newclient:
    return update_client(client_id, new_client)


@router.delete("/{client_id}")
def delete_client(client_id: int) -> Newclient:
    return delete_current_client(client_id)