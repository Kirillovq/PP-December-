from typing import Optional
from pydantic import BaseModel

class ImputOrders(BaseModel):
    id: int
    date_create: str
    object: str
    type_repair: str
    description_object: str
    client: Optional[int]
    date_end: str
    executor: Optional[int]

class OutputOrders(BaseModel):
    id: int
    date_create: str
    object: str
    type_repair: str
    description_object: str
    client: Optional[int]
    date_end: str
    executor: Optional[int]

class NewId(BaseModel):
    id: int
    date_create: str
    object: str
    type_repair: str
    description_object: str
    client: Optional[int]
    date_end: str
    executor: Optional[int]
