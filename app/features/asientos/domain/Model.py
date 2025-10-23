# Pydantic
from pydantic import BaseModel


class AsientosModel(BaseModel):
    codigo: int
    asiento: str
    codigo_avion: int


    class Config:
        from_attributes = True
