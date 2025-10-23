# Pydantic
from pydantic import BaseModel


class SendDTO(BaseModel):
    codigo_reserva: int
    codigo_pasajero: int
    codigo_asiento: int
