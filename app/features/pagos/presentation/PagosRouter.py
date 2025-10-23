# FastAPI
from fastapi import APIRouter
# UOW
from app.core.unit_of_work import UnitOfWork
# Application
from app.features.pagos.application.GetAll import GetAll
from app.features.pagos.application.Add import Add
# DTOs
from app.features.pagos.DTOs.SendDTO import SendDTO


router = APIRouter()


@router.get('/pagos')
async def get_all():
    async with UnitOfWork() as uow:
        use_case = GetAll(uow)
        return await use_case.execute_async()
    
    
@router.post('/pagos')
async def add(payment: SendDTO):
    async with UnitOfWork() as uow:
        use_case = Add(uow)
        return await use_case.execute_async(payment)
