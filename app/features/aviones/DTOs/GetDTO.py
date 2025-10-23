# Pydantic
from pydantic import BaseModel


class GetDTO(BaseModel):
    codigo: int
    marca: str
    marca: str
    capacidad: int


    class Config:
        from_attributes = True
