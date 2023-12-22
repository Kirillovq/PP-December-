from .models import OutputOrders, ImputOrders, NewId
from db_manager import base_manager

ID = 0
DATE_CREATE = 1
OBJECT = 2
TYPE_REPAIR = 3
DESCRIPTION_OBJECT = 4
CLIENT = 5
DATE_END = 6
EXECUTOR = 7



def get_orderss():
    res = base_manager.execute("SELECT id, date_create, object ,type_repair, description_object, client, date_end, executor FROM orders", many=True)
    orders = []
    for orders in res['data']:
        orders.append(OutputOrders(id=orders[ID], date_create=orders[DATE_CREATE],object=orders[OBJECT],type_repair=orders[TYPE_REPAIR],description_object=orders[DESCRIPTION_OBJECT],client=orders[CLIENT],date_end=orders[DATE_END],executor=orders[EXECUTOR]))
    return orders


def get_orders(orders_id: int):
    res = base_manager.execute("SELECT id, date_create, object ,type_repair, description_object, client, date_end, executor FROM orders WHERE id = ?",
                               args=(orders_id,), many=False)
    print(res)
    return OutputOrders()


def add_new_orders(new_orders: ImputOrders, ):
    res = base_manager.execute("INSERT INTO orders(id, date_create, object ,type_repair, description_object, client, date_end, executor) "
                               "VALUES (?,?,?,?,?,?,?) "
                               "RETURNING id", args=(new_orders.id,new_orders.date_create,new_orders.object,new_orders.type_repair, new_orders.description_object,new_orders.client,new_orders.date_end,new_orders.executor,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_orders(orders_id: int, orders: ImputOrders):
    res = base_manager.execute("UPDATE orders SET date_create = ?, object = ? ,type_repair = ?,  description_object = ?, client = ?, date_end = ?, executor = ?  WHERE id = ?",
                               args=(orders.date_create, orders.object, orders.type_repair, orders.description_object, orders.client, orders.date_end,orders.executor, ))
    return NewId(code=res['code'], id=orders_id)


def delete_current_orders(orders_id: int):
    res = base_manager.execute("DELETE FROM orders WHERE id = ?",
                               args=(orders_id,))
    return NewId(code=res['code'], id=orders_id)