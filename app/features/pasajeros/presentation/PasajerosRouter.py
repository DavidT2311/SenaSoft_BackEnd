# FastAPI
from fastapi import APIRouter
# UOW
from app.core.unit_of_work import UnitOfWork
# Application
from app.features.pasajeros.application.GetAll import GetAll
from app.features.pasajeros.application.Add import Add
# DTOs
from app.features.pasajeros.DTOs.PassengerListDTO import PassengerListDTO


router = APIRouter()


@router.get('/pasajeros')
async def get_all():
    async with UnitOfWork() as uow:
        use_case = GetAll(uow)
        return await use_case.execute_async()
    
    
@router.post('/pasajeros')
async def add(passenger_list: PassengerListDTO):
    async with UnitOfWork() as uow:
        use_case = Add(uow)
        return await use_case.execute_async(passenger_list)
