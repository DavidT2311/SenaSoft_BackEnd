# Pydantic
from pydantic import BaseModel
# Python
from datetime import date
from typing import Optional
# DTOs
from app.features.pasajeros.DTOs.EnumGenero import EnumGenero


class SendDTO(BaseModel):
    tipo_documento: str
    documento: str
    primer_apellido: str
    segundo_apellido: str
    nombres: str
    correo: str
    celular: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[EnumGenero] = None
    infante: Optional[bool] = None
    asiento: int
