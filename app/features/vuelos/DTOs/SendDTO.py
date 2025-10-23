# Pydantic
from pydantic import BaseModel
# Python
from datetime import date, time
from decimal import Decimal
from typing import Optional
# DTOs
from app.features.vuelos.DTOs.EnumTipoVuelo import EnumTipoVuelo

class SendDTO(BaseModel):
    origen: str
    destino: str
    fecha_ida: date
    hora_ida: time
    fecha_regreso: Optional[date]
    hora_regreso: Optional[time]
    precio: Decimal
    tipo_vuelo: EnumTipoVuelo

    codigo_avion: int


    class Config:
        json_encoders = {
            Decimal: lambda v: format(v, "f")
        }
