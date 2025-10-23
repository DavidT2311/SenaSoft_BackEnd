# Python
from enum import Enum


class EnumTipoPago(str, Enum):
    Credito = 'Tarjeta de crédito' 
    Debito = 'Tarjeta de débito'
    PSE = 'PSE'
