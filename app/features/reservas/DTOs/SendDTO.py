# Pydantic
from pydantic import BaseModel
# Python
from typing import List
from datetime import date
# DTOs
from app.features.reservas.DTOs.PasajeroAsientoDTO import PasajeroAsientoDTO


class SendDTO(BaseModel):
    codigo_vuelo: int
    fecha: date
    pasajeros: List['PasajeroAsientoDTO']
