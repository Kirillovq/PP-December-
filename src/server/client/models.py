from typing import Optional
from pydantic import BaseModel

class Imputclient(BaseModel):
    id_client: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str

class Outputclient(BaseModel):
    id_client: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str

class Newclient(BaseModel):
    id_client: int
    name: Optional[str]
    surname: Optional[str]
    number_telephone: Optional[str]
    address: str
    email: str