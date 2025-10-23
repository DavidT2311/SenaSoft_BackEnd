# Pydantic
from pydantic import BaseModel
# Python
from datetime import date


class GetDTO(BaseModel):
    codigo: int
    codigo_vuelo: int
    fecha: date


    class Config:
        from_attributes = True
