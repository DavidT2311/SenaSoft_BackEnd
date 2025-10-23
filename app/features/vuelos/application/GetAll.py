# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.vuelos.infrastructure.Repository import Repository
# Application
from app.features.asientos.application.GetSeatsByPlaneCode import GetSeatsByPlaneCode
from app.features.aviones.application.GetById import GetByCode as GetPlaneByCode
# DTOs
from app.features.vuelos.DTOs.EnumTipoVuelo import EnumTipoVuelo
# Python
from typing import Optional
from datetime import date


class GetAll:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(
            self, 
            ida: Optional[EnumTipoVuelo], 
            orig: Optional[str], 
            dest: Optional[str], 
            fida: Optional[date], 
            freg: Optional[date]
            ):
        # get_seats_by_plane_code = GetSeatsByPlaneCode(self.uow)
        get_plane_by_code = GetPlaneByCode(self.uow)

        flights_list = await self.repository.get_all(ida, orig, dest, fida, freg)

        for flight in flights_list:
            plane = await get_plane_by_code.execute_async(flight.codigo_avion)
            flight.capacidad = plane.capacidad

        # plane = await get_plane_by_code.execute_async(flights_list[0].codigo_avion)
        # seats_list = await get_seats_by_plane_code.execute_async(flights_list[0].codigo_avion)

        # flights_list_filtered = []

        # for flight in flights_list:
        #     if (plane.capacidad >= len(seats_list)):
        #         continue
            
        #     flights_list_filtered.append(flight)

        return flights_list# flights_list_filtered
        