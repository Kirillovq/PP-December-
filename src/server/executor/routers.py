from typing import List

from fastapi import APIRouter
from .models import ImputExecutor, OutputExecutor, NewId
from .resolvers import get_executors, get_executor, add_new_executor, update_executor, delete_current_executor


router = APIRouter()


@router.get('/')
def get_executor() -> List[OutputExecutor]:
    return get_executors()


@router.get('/{executor_id}')
def get_current_executor(executor_id: int) -> OutputExecutor:
    return get_executor(executor_id)


@router.post('/')
def add_executor(new_executor: ImputExecutor) -> NewId:
    return add_new_executor(new_executor)


@router.put('/{executor_id}')
def add_executor(executor_id: int, new_executor: ImputExecutor) -> NewId:
    return update_executor(executor_id, new_executor)


@router.delete("/{executor_id}")
def delete_executor(executor_id: int) -> NewId:
    return delete_current_executor(executor_id)