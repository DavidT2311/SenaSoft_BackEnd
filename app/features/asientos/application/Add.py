# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.asientos.infrastructure.Repository import Repository
# Application
from app.features.aviones.application.GetById import GetByCode as GetPlaneByCode
from app.features.vuelos.application.GetById import GetByCode as GetFlightByCode
# DTOs
from app.features.asientos.DTOs.SendDTO import SendDTO
# FastAPI
from fastapi.exceptions import HTTPException


class Add:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(self, seat: SendDTO):
        get_plane_by_code = GetPlaneByCode(self.uow)
        # get_flight_by_code = GetFlightByCode(self.uow)

        # Validacion que el asiento sea un numero positivo
        if seat.asiento <= 0:
            raise HTTPException(404, "El asiento es invalido")

        # # Llamamos al caso de uso de obtener vuelo por codigo
        # flight = await get_flight_by_code.execute_async(seat.codigo_vuelo)
        
        # # Validamos que el vuelo exista
        # if not flight:
        #     raise HTTPException(404, "No se encontro el vuelo")
        
        # Llamamos al caso de uso de obtener avion por codigo
        plane = await get_plane_by_code.execute_async(seat.codigo_avion)

        # Validamos que el avion exista
        if not plane:
            raise HTTPException(404, "No se encontro el avion")
        
        seats_list = await self.repository.get_seats_by_plane_code(seat.codigo_avion)

        # Validamos que el asiento no supere la capacidad del avion
        if len(seats_list) > plane.capacidad:
            raise HTTPException(400, "El asiento esta fuera de la capacidad del avion")

        # Validamos que el asiento no exista
        for seat_in_list in seats_list:
            if seat_in_list.asiento == seat.asiento:
                raise HTTPException(400, "El asiento ya existe")

        return await self.repository.add(seat)
        