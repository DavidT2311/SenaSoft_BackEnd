# FastAPI
from fastapi import APIRouter
# UOW
from app.core.unit_of_work import UnitOfWork
# Application
from app.features.vuelos.application.GetAll import GetAll
# from app.features.vuelos.application.Add import Add
# DTOs
from app.features.vuelos.DTOs.SendDTO import SendDTO
from app.features.vuelos.DTOs.EnumTipoVuelo import EnumTipoVuelo
# Python
from datetime import date
from typing import Optional

router = APIRouter()


@router.get('/vuelos')
async def get_all(
    ida: Optional[EnumTipoVuelo] = None, 
    orig: Optional[str] = None, 
    dest: Optional[str] = None, 
    fida: Optional[date] = None, 
    freg: Optional[date] = None
    ):
    async with UnitOfWork() as uow:
        use_case = GetAll(uow)
        return await use_case.execute_async(ida, orig, dest, fida, freg)
    
    
# @router.post('/products')
# async def add(product: SendDTO):
#     async with UnitOfWork() as uow:
#         use_case = Add(uow)
#         return await use_case.execute_async(product)
