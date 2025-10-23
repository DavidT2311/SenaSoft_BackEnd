# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.reservas.infrastructure.Repository import Repository
# Application
from app.features.tiquetes.application.Add import Add as AddTicket
# DTOs
from app.features.reservas.DTOs.SendDTO import SendDTO
from app.features.tiquetes.DTOs.SendDTO import SendDTO as SendTicketDTO


class Add:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(self, reservation: SendDTO):
        add_ticket = AddTicket(self.uow)

        added_reservation = await self.repository.add(reservation)

        for passenger in reservation.pasajeros:
            send_ticket_dto = SendTicketDTO(
                codigo_reserva=added_reservation.codigo,
                codigo_asiento=passenger.codigo_asiento,
                codigo_pasajero=passenger.codigo_pasajero
                )

            await add_ticket.execute_async(send_ticket_dto)

        return added_reservation
