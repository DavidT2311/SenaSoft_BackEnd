# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Context
from app.context.SenaSoftContext import Pasajeros
# DTOs
from app.features.pasajeros.DTOs.GetDTO import GetDTO
from app.features.pasajeros.DTOs.SendDTO import SendDTO
# Model
from app.features.pasajeros.domain.Model import PassengerModel


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        passengers_list = await self.db.execute(select(Pasajeros))
        passengers_list = passengers_list.scalars().all()

        return [GetDTO.model_validate(passenger) for passenger in passengers_list]

    async def add(self, passenger: SendDTO):
        new_passenger = Pasajeros(**passenger.dict(exclude={'asiento'}))
        self.db.add(new_passenger)

        try:
            await self.db.flush()
            return PassengerModel.model_validate(new_passenger)
        except:
            raise

    async def get_by_code(self, code: int):
        passenger = await self.__get_by_code(code)

        if not passenger:
            raise

        return PassengerModel.model_validate(passenger)

    async def __get_by_code(self, code: int):
        passenger = await self.db.execute(select(Pasajeros).where(Pasajeros.codigo == code))
        passenger = passenger.scalars().first()

        if not passenger:
            raise

        return passenger
    
    async def get_by_email(self, email: str):
        passenger = await self.db.execute(select(Pasajeros).where(Pasajeros.correo == email))
        passenger = passenger.scalars().first()

        if not passenger:
            return None

        return passenger

