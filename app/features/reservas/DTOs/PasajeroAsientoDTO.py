
# Pydantic
from pydantic import BaseModel
# Python
from datetime import date
from typing import Optional
# DTOs
from app.features.pasajeros.DTOs.EnumGenero import EnumGenero


class PasajeroAsientoDTO(BaseModel):
    codigo_pasajero: int
    codigo_asiento: int
