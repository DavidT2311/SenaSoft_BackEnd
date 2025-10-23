# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
# Context
from app.context.SenaSoftContext import Aviones
# DTOs
from app.features.aviones.DTOs.GetDTO import GetDTO
from app.features.aviones.DTOs.SendDTO import SendDTO
# Model
from app.features.aviones.domain.Model import AvionesModel


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List['GetDTO']:
        planes_list = await self.db.execute(select(Aviones))
        planes_list = planes_list.scalars().all()

        return [GetDTO.model_validate(plane) for plane in planes_list]
    

    async def add(self, plane: SendDTO):
        new_plane = Aviones(**plane.dict())
        self.db.add(new_plane)

        try:
            await self.db.flush()
            return AvionesModel.model_validate(new_plane)
        except:
            raise

    async def get_by_code(self, code: int):
        plane = await self.__get_by_code(code)

        if not plane:
            raise

        return AvionesModel.model_validate(plane)

   
    async def __get_by_code(self, code: int):
        plane = await self.db.execute(select(Aviones).where(Aviones.codigo == code))
        plane = plane.scalars().first()

        if not plane:
            raise

        return plane

