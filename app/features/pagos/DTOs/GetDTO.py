# Pydantic
from pydantic import BaseModel
# Python
from datetime import date
from typing import Optional
from decimal import Decimal
# DTOs
from app.features.pagos.DTOs.EnumTipoPago import EnumTipoPago


class GetDTO(BaseModel):
    codigo: int
    tipo_documento: str
    documento: str 
    nombre_completo: str
    correo: str
    monto: Decimal
    codigo_reserva: int
    celular: Optional[str] = None
    tipo_pago: str = EnumTipoPago
    numero_tarjeta: Optional[str] = None
    caducidad: Optional[date] = None
    cvv: Optional[int] = None


    class Config:
        from_attributes = True
        json_encoders = {
            Decimal: lambda v: format(v, "f")
        }
