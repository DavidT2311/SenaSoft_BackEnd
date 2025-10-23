# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Context
from app.context.SenaSoftContext import Asientos
# DTOs
from app.features.asientos.DTOs.GetDTO import GetDTO
from app.features.asientos.DTOs.SendDTO import SendDTO
# Model
from app.features.asientos.domain.Model import AsientosModel


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        seats_list = await self.db.execute(select(Asientos))
        seats_list = seats_list.scalars().all()

        return [GetDTO.model_validate(seats) for seats in seats_list]

    async def add(self, seat: SendDTO):
        new_seat = Asientos(**seat.dict())
        self.db.add(new_seat)

        try:
            await self.db.flush()
            return AsientosModel.model_validate(new_seat)
        except:
            raise

    async def get_seats_by_plane_code(self, code: int):
        seats = await self.db.execute(
            select(Asientos)
            .where(Asientos.codigo_avion == code)
        )

        seats = seats.scalars().all()

        if not seats:
            raise

        return seats
