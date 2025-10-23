# Python
import datetime
import decimal
# SQLAlchemy
from sqlalchemy import BigInteger, Boolean, Date, Enum, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Time, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
# Core
from app.core.database import Base


class Aviones(Base):
    __tablename__ = 'aviones'
    __table_args__ = (
        PrimaryKeyConstraint('codigo', name='aviones_pkey'),
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    marca: Mapped[str] = mapped_column(String(250), nullable=False)
    modelo: Mapped[str] = mapped_column(String(250), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)

    vuelos: Mapped[list['Vuelos']] = relationship('Vuelos', back_populates='aviones')
    asientos: Mapped[list['Asientos']] = relationship('Asientos', back_populates='aviones')


class Pasajeros(Base):
    __tablename__ = 'pasajeros'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pasajeros_pkey'),
        UniqueConstraint('correo', name='pasajeros_correo_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    tipo_documento: Mapped[str] = mapped_column(String(250), nullable=False)
    documento: Mapped[str] = mapped_column(String(250), nullable=False)
    primer_apellido: Mapped[str] = mapped_column(String(250), nullable=False)
    segundo_apellido: Mapped[str] = mapped_column(String(250), nullable=False)
    nombres: Mapped[str] = mapped_column(String(250), nullable=False)
    correo: Mapped[str] = mapped_column(String(250), nullable=False)
    celular: Mapped[str] = mapped_column(String(16))
    fecha_nacimiento: Mapped[datetime.date] = mapped_column(Date)
    genero: Mapped[str] = mapped_column(Enum('Masculino', 'Femenino', name='genero'))
    infante: Mapped[bool] = mapped_column(Boolean)

    tiquetes: Mapped[list['Tiquetes']] = relationship('Tiquetes', back_populates='pasajeros')


class Usuarios(Base):
    __tablename__ = 'usuarios'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='usuarios_pkey'),
        UniqueConstraint('correo', name='usuarios_correo_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    correo: Mapped[str] = mapped_column(String(250), nullable=False)
    clave: Mapped[str] = mapped_column(String(250))


class Vuelos(Base):
    __tablename__ = 'vuelos'
    __table_args__ = (
        ForeignKeyConstraint(['codigo_avion'], ['aviones.codigo'], name='vuelos_codigo_avion_fkey'),
        PrimaryKeyConstraint('codigo', name='vuelos_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    origen: Mapped[str] = mapped_column(String(250), nullable=False)
    destino: Mapped[str] = mapped_column(String(250), nullable=False)
    fecha_ida: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    hora_ida: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    fecha_regreso: Mapped[datetime.date] = mapped_column(Date)
    hora_regreso: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    precio: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 0), nullable=False)
    tipo_vuelo: Mapped[str] = mapped_column(Enum('Solo ida', 'Ida y regreso', name='tipo_vuelo'))
    codigo_avion: Mapped[int] = mapped_column(BigInteger)

    aviones: Mapped['Aviones'] = relationship('Aviones', back_populates='vuelos')
    reservas: Mapped[list['Reservas']] = relationship('Reservas', back_populates='vuelos')


class Asientos(Base):
    __tablename__ = 'asientos'
    __table_args__ = (
        ForeignKeyConstraint(['codigo_avion'], ['aviones.codigo'], name='asientos_codigo_avion_fkey'),
        PrimaryKeyConstraint('codigo', name='asientos_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    asiento: Mapped[str] = mapped_column(String(250 ))
    codigo_avion: Mapped[int] = mapped_column(BigInteger)

    aviones: Mapped['Aviones'] = relationship('Aviones', back_populates='asientos')
    tiquetes: Mapped['Tiquetes'] = relationship('Tiquetes', back_populates='asientos')


class Reservas(Base):
    __tablename__ = 'reservas'
    __table_args__ = (
        ForeignKeyConstraint(['codigo_vuelo'], ['vuelos.codigo'], name='reservas_codigo_vuelo_fkey'),
        PrimaryKeyConstraint('codigo', name='reservas_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    fecha: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    codigo_vuelo: Mapped[int] = mapped_column(BigInteger)

    vuelos: Mapped['Vuelos'] = relationship('Vuelos', back_populates='reservas')
    pagos: Mapped[list['Pagos']] = relationship('Pagos', back_populates='reservas')
    tiquetes: Mapped[list['Tiquetes']] = relationship('Tiquetes', back_populates='reservas')


class Pagos(Base):
    __tablename__ = 'pagos'
    __table_args__ = (
        ForeignKeyConstraint(['codigo_reserva'], ['reservas.codigo'], name='pagos_codigo_reserva_fkey'),
        PrimaryKeyConstraint('codigo', name='pagos_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    tipo_documento: Mapped[str] = mapped_column(String(250), nullable=False)
    documento: Mapped[str] = mapped_column(String(250), nullable=False)
    nombre_completo: Mapped[str] = mapped_column(String(250), nullable=False)
    correo: Mapped[str] = mapped_column(String(250), nullable=False)
    monto: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 0), nullable=False)
    codigo_reserva: Mapped[int] = mapped_column(BigInteger)
    celular: Mapped[str] = mapped_column(String(16))
    tipo_pago: Mapped[str] = mapped_column(Enum('Tarjeta de crédito', 'Tarjeta de débito', 'PSE', name='tipo_pago'))
    numero_tarjeta: Mapped[str] = mapped_column(String(250), nullable=True)
    caducidad: Mapped[datetime.date] = mapped_column(Date, nullable=True)
    cvv: Mapped[int] = mapped_column(Integer, nullable=True)

    reservas: Mapped['Reservas'] = relationship('Reservas', back_populates='pagos')


class Tiquetes(Base):
    __tablename__ = 'tiquetes'
    __table_args__ = (
        ForeignKeyConstraint(['codigo_pasajero'], ['pasajeros.id'], name='tiquetes_codigo_pasajero_fkey'),
        ForeignKeyConstraint(['codigo_reserva'], ['reservas.codigo'], name='tiquetes_codigo_reserva_fkey'),
        ForeignKeyConstraint(['codigo_asiento'], ['asientos.codigo'], name='tiquetes_codigo_asiento_fkey'),
        PrimaryKeyConstraint('codigo', name='tiquetes_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    codigo_reserva: Mapped[int] = mapped_column(BigInteger)
    codigo_pasajero: Mapped[int] = mapped_column(BigInteger)
    codigo_asiento: Mapped[int] = mapped_column(BigInteger)

    pasajeros: Mapped['Pasajeros'] = relationship('Pasajeros', back_populates='tiquetes')
    reservas: Mapped['Reservas'] = relationship('Reservas', back_populates='tiquetes')
    asientos: Mapped['Asientos'] = relationship('Asientos', back_populates='tiquetes')
