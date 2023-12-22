from .models import OutputClient, ImputClient, NewId
from db_manager import base_manager

ID = 0
NAME = 1


def get_clients():
    res = base_manager.execute("SELECT id,name,surname,number_telephone,address,email FROM client", many=True)
    client = []
    for client in res['data']:
        client.append(OutputClient(id=client[ID], name=client[NAME]))
    return client


def get_client(client_id: int):
    res = base_manager.execute("SELECT id,name,surname,number_telephone,address,email FROM client WHERE id = ?",
                               args=(client_id,), many=False)
    print(res)
    return OutputClient()


def add_new_client(new_client: ImputClient, ):
    res = base_manager.execute("INSERT INTO client(name,surname,number_telephone,address,email) "
                               "VALUES (?,?,?,?,?) "
                               "RETURNING id", args=(new_client.name,new_client.surname,new_client.number_telephone,new_client.address,new_client.email,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_client(client_id: int, client: ImputClient):
    res = base_manager.execute("UPDATE client SET name = ? WHERE id = ?",
                               args=(client.name, client_id, ))
    return NewId(code=res['code'], id=client_id)


def delete_current_client(client_id: int):
    res = base_manager.execute("DELETE FROM client WHERE id = ?",
                               args=(client_id,))
    return NewId(code=res['code'], id=client_id)