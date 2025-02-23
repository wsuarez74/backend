from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True)
    credito_disponible = Column(Float)

class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    monto = Column(Float)

class Cobranza(Base):
    __tablename__ = "cobranzas"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    deuda = Column(Float)  # Monto de deuda

