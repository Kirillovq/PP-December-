from .models import Outputclient, Imputclient, Newclient
from db_manager import base_manager

#ID_CLIENT = 0
#NAME = 1
#SURNAME = 2
#NUMBER_TELEPHONE = 3
#ADDRESS = 4
#EMAIL = 5

def get_clients():
    res = base_manager.execute("SELECT id_client,name,surname,number_telephone,address,email FROM client", many=True)
    client = []
    for client in res['data']:
        client.append(Outputclient)
    return client


#def get_client(client_id: int):
#    res = base_manager.execute("SELECT id, name FROM groups WHERE id = ?",
#                               args=(client_id,), many=False)
#    print(res)
#    return Outputclient(id=res["id"], name=res["name"])


#def add_new_client(new_client Imputclient, ):
#    res = base_manager.execute("INSERT INTO client(name) "
#                               "VALUES (?) "
#                               "RETURNING id", args=(new_client.name,))
#    print(res)
#    return Newclient(code=res['code'], id=res['data'][0][0])


#def update_client(group_id: int, group: ImputGroup):
#    res = base_manager.execute("UPDATE groups SET name = ? WHERE id = ?",
#                               args=(group.name, group_id,))
#    return NewId(code=res['code'], id=group_id)


#def delete_current_client(group_id: int):
#    res = base_manager.execute("DELETE FROM groups WHERE id = ?",
#                               args=(group_id,))
#    return NewId(code=res['code'], id=group_id)