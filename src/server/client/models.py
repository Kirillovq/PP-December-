from typing import Optional
from pydantic import BaseModel

class ImputClient(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str

class OutputClient(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str

class NewId(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str