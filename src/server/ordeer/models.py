from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    login: str
    password: str
    post: Optional[int]
    reg_date: Optional[datetime]

class client(BaseModel):
    id_client: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str

class executor(BaseModel):
    id_executor: Optional[int]
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    object_management: str

class oredeer(BaseModel):
    id_ordeer: int
    date_create: Optional[datetime]
    object: str
    type_repair: str
    description_object: str
    client: Optional[int]
    date_end: Optional[datetime]
    executor: Optional[int]
