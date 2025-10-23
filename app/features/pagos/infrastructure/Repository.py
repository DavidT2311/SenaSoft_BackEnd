# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Context
from app.context.SenaSoftContext import Pagos
# DTOs
from app.features.pagos.DTOs.GetDTO import GetDTO
from app.features.pagos.DTOs.SendDTO import SendDTO
# Model
from app.features.pagos.domain.Model import PaymentsModel


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        payments_list = await self.db.execute(select(Pagos))
        payments_list = payments_list.scalars().all()

        return [GetDTO.model_validate(payment) for payment in payments_list]

    async def add(self, payment: SendDTO):
        new_payment = Pagos(**payment.dict())
        self.db.add(new_payment)

        try:
            await self.db.flush()
            return PaymentsModel.model_validate(new_payment)
        except:
            raise

    async def get_by_code(self, code: int):
        payment = await self.__get_by_code(code)

        if not payment:
            raise

        return PaymentsModel.model_validate(payment)

    async def __get_by_code(self, code: int):
        payment = await self.db.execute(select(Pagos).where(Pagos.codigo == code))
        payment = payment.scalars().first()

        if not payment:
            raise

        return payment

