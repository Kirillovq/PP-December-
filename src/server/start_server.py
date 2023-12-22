from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from db_manager import base_manager
from client import router as client_router
from executor import router as executor_router
from orders import router as orders_router
#from users import router as users_router
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH

app = FastAPI()

#app.include_router(users_router, prefix='/users')
app.include_router(client_router, prefix='/client')
app.include_router(executor_router, prefix='/executor')
app.include_router(orders_router, prefix='/orders')



@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)