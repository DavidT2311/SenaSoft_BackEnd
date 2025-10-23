# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.tiquetes.infrastructure.Repository import Repository
# Application
from app.features.tiquetes.application.GetTicketBySeatCode import GetTicketBySeatCode
# DTOs
from app.features.tiquetes.DTOs.SendDTO import SendDTO
# FastApi
from fastapi import HTTPException


class Add:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(self, ticket: SendDTO):
        get_ticket_by_seat_code = GetTicketBySeatCode(self.uow)

        seat = await get_ticket_by_seat_code.execute_async(ticket.codigo_asiento)

        if seat:
            raise HTTPException(400, "El asiento ya esta ocupado")

        return await self.repository.add(ticket)
        