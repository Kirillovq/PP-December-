from typing import Optional
from pydantic import BaseModel

class ImputExecutor(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    object_management: Optional[str]


class OutputExecutor(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    object_management: Optional[str]


class NewId(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    object_management: Optional[str]