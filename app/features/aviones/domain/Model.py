# Pydantic
from pydantic import BaseModel


class AvionesModel(BaseModel):
    codigo: int
    marca: str
    marca: str
    capacidad: int


    class Config:
        from_attributes = True
