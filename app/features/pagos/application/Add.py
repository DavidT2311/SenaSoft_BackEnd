# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.pagos.infrastructure.Repository import Repository
# DTOs
from app.features.pagos.DTOs.SendDTO import SendDTO
# FastAPI
from fastapi import HTTPException


class Add:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(self, payment: SendDTO):
        if (payment.monto <= 0):
            raise HTTPException(400, "El monto es invalido") 

        return await self.repository.add(payment)
