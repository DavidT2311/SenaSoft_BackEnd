# Pydantic
from pydantic import BaseModel
# Python
from datetime import date
from typing import Optional
# DTOs
from app.features.pasajeros.DTOs.EnumGenero import EnumGenero


class GetDTO(BaseModel):
    id: int
    tipo_documento: str
    documento: str
    primer_apellido: str
    segundo_apellido: str
    nombres: str
    correo: str
    celular: Optional[str]
    fecha_nacimiento: Optional[date]
    genero: Optional[EnumGenero]
    infante: Optional[bool]


    class Config:
        from_attributes = True
