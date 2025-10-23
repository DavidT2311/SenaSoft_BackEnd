# Pydantic
from pydantic import BaseModel
# Python
from datetime import date


class ReservasModel(BaseModel):
    codigo: int
    codigo_vuelo: int
    fecha: date


    class Config:
        from_attributes = True
