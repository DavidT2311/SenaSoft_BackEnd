# Pydantic
from pydantic import BaseModel
# Python
from datetime import date
from typing import Optional, List
# DTOs
from app.features.pasajeros.DTOs.SendDTO import SendDTO


class PassengerListDTO(BaseModel):
    lista_pasajeros: List['SendDTO']
