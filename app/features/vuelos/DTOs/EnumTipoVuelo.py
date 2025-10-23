# Python
from enum import Enum


class EnumTipoVuelo(str, Enum):
    Ida = 'Solo ida' 
    Regreso = 'Ida y regreso'
