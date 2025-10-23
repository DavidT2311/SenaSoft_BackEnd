# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Context
from app.context.SenaSoftContext import Tiquetes
# DTOs
from app.features.tiquetes.DTOs.GetDTO import GetDTO
from app.features.tiquetes.DTOs.SendDTO import SendDTO
# Model
from app.features.tiquetes.domain.Model import TiquetesModel


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        tickets_list = await self.db.execute(select(Tiquetes))
        tickets_list = tickets_list.scalars().all()

        return [GetDTO.model_validate(ticket) for ticket in tickets_list]

    async def add(self, ticket: SendDTO):
        new_ticket = Tiquetes(**ticket.dict())
        self.db.add(new_ticket)

        try:
            await self.db.flush()
            return TiquetesModel.model_validate(new_ticket)
        except:
            raise

    async def get_by_code(self, code: int):
        ticket = await self.__get_by_code(code)

        if not ticket:
            raise

        return TiquetesModel.model_validate(ticket)

    async def __get_by_code(self, code: int):
        ticket = await self.db.execute(select(Tiquetes).where(Tiquetes.codigo == code))
        ticket = ticket.scalars().first()

        if not ticket:
            raise

        return ticket
    
    async def get_ticket_by_seat_code(self, code: int):
        ticket = await self.db.execute(select(Tiquetes).where(Tiquetes.codigo_asiento == code))
        ticket = ticket.scalars().first()

        if not ticket:
            return None

        return ticket

