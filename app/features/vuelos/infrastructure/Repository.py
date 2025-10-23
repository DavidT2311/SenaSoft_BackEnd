# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, String, func
# Context
from app.context.SenaSoftContext import Vuelos
# DTOs
from app.features.vuelos.DTOs.GetDTO import GetDTO
from app.features.vuelos.DTOs.SendDTO import SendDTO
from app.features.vuelos.DTOs.EnumTipoVuelo import EnumTipoVuelo
# Model
from app.features.vuelos.domain.Model import VuelosModel
# Python
from typing import Optional
from datetime import date


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(
            self, 
            ida: Optional[EnumTipoVuelo], 
            orig: Optional[str], 
            dest: Optional[str], 
            fida: Optional[date], 
            freg: Optional[date]
            ):
        
        query = select(Vuelos) 

        if ida:
            query = query.where(Vuelos.tipo_vuelo == ida)

        if orig:
            query = query.where(func.lower(Vuelos.origen) == orig.lower())

        if dest:
            query = query.where(func.lower(Vuelos.destino) == dest.lower())

        if fida:
            query = query.where(Vuelos.fecha_ida == fida)

        if freg:
            query = query.where(Vuelos.fecha_regreso == freg)

        flights_list = await self.db.execute(query)

        flights_list = flights_list.scalars().all()

        return [GetDTO.model_validate(flight) for flight in flights_list]

    async def add(self, flight: SendDTO):
        new_flight = Vuelos(**flight.dict())
        self.db.add(new_flight)

        try:
            await self.db.flush()
            return VuelosModel.model_validate(new_flight)
        except:
            raise

    async def get_by_code(self, code: int):
        flight = await self.__get_by_code(code)

        if not flight:
            raise

        return VuelosModel.model_validate(flight)

    async def __get_by_code(self, code: int):
        flight = await self.db.execute(select(Vuelos).where(Vuelos.codigo == code))
        flight = flight.scalars().first()

        if not flight:
            raise

        return flight

