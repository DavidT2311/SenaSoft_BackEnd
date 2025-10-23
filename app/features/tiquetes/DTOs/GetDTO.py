# Pydantic
from pydantic import BaseModel


class GetDTO(BaseModel):
    codigo: int
    codigo_reserva: int
    codigo_pasajero: int
    codigo_asiento: int

    class Config:
        from_attributes = True
