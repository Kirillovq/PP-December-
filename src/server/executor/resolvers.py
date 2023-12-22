from .models import OutputExecutor, ImputExecutor, NewId
from db_manager import base_manager

ID = 0
NAME = 1
SURNAME = 2
number_telephone = 3
object_management = 4


def get_executors():
    res = base_manager.execute("SELECT id, name, surname,number_telephone, object_management FROM executor", many=True)
    executor = []
    for executor in res['data']:
        executor.append(OutputExecutor(id=executor[ID], name=executor[NAME]))
    return executor


def get_executor(executor_id: int):
    res = base_manager.execute("SELECT id, name, surname,number_telephone, object_management FROM executor WHERE id = ?",
                               args=(executor_id,), many=False)
    print(res)
    return OutputExecutor()


def add_new_executor(new_executor: ImputExecutor, ):
    res = base_manager.execute("INSERT INTO executor(id, name, surname,number_telephone, object_management) "
                               "VALUES (?,?,?,?,?) "
                               "RETURNING id", args=(new_executor.id,new_executor.name,new_executor.surname,new_executor.number_telephone,new_executor.object_management,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_executor(executor_id: int, executor: ImputExecutor):
    res = base_manager.execute("UPDATE executor SET name = ? WHERE id = ?",
                               args=(executor.name, executor_id,))
    return NewId(code=res['code'], id=executor_id)


def delete_current_executor(executor_id: int):
    res = base_manager.execute("DELETE FROM executor WHERE id = ?",
                               args=(executor_id,))
    return NewId(code=res['code'], id=executor_id)