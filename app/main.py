# Uvicorn
import uvicorn
# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Settings
from app.core.settings import settings
# Vuelos
from app.features.vuelos.presentation import VuelosRouter
# Asientos
from app.features.asientos.presentation import AsientosRouter
# Reservas
from app.features.reservas.presentation import ReservasRouter
# Tiquetes
from app.features.tiquetes.presentation import TiquetesRouter
# Pasajeros
from app.features.pasajeros.presentation import PasajerosRouter
# Pagos
from app.features.pagos.presentation import PagosRouter
# aviones
# from app.features.aviones.presentation import AvionesRouter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ruta aviones 
# app.include_router(AvionesRouter.router, prefix="/api/v1", tags=["Aviones"])
# Ruta vuelos 
app.include_router(VuelosRouter.router, prefix="/api/v1", tags=["Vuelos"])
# Ruta asientos 
app.include_router(AsientosRouter.router, prefix="/api/v1", tags=["Asientos"])
# Ruta reservas 
app.include_router(ReservasRouter.router, prefix="/api/v1", tags=["Reservas"])
# Ruta tiquetes 
app.include_router(TiquetesRouter.router, prefix="/api/v1", tags=["Tiquetes"])
# Ruta pasajeros 
app.include_router(PasajerosRouter.router, prefix="/api/v1", tags=["Pasajeros"])
# Ruta pagos 
app.include_router(PagosRouter.router, prefix="/api/v1", tags=["Pagos"])


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
