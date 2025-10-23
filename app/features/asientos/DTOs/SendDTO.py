# Pydantic
from pydantic import BaseModel


class SendDTO(BaseModel):
    asiento: str
    codigo_avion: int
