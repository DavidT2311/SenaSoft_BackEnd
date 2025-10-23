# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Context
from app.context.SenaSoftContext import Reservas
# DTOs
from app.features.reservas.DTOs.GetDTO import GetDTO
from app.features.reservas.DTOs.SendDTO import SendDTO
# Model
from app.features.reservas.domain.Model import ReservasModel


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        reservations_list = await self.db.execute(select(Reservas))
        reservations_list = reservations_list.scalars().all()

        return [GetDTO.model_validate(reservation) for reservation in reservations_list]

    async def add(self, reservation: SendDTO):
        new_reservation = Reservas(**reservation.dict(exclude={'pasajeros'}))
        self.db.add(new_reservation)

        try:
            await self.db.flush()
            return ReservasModel.model_validate(new_reservation)
        except:
            raise

    async def get_by_code(self, code: int):
        reservation = await self.__get_by_code(code)

        if not reservation:
            raise

        return ReservasModel.model_validate(reservation)

    async def __get_by_code(self, code: int):
        reservation = await self.db.execute(select(Reservas).where(Reservas.codigo == code))
        reservation = reservation.scalars().first()

        if not reservation:
            raise

        return reservation

