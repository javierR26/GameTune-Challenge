# backend/models/juego_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.db import Base

class Juegos(Base):
    __tablename__ = "Juego"

    Id = Column(Integer, primary_key=True, index=True)
    Audio = Column(String(250), nullable=False)
    Nombre = Column(String(250), nullable=False)

    opciones = relationship("Opciones", back_populates="juego")


class Opciones(Base):
    __tablename__ = "Opciones"

    Id = Column(Integer, primary_key=True, index=True)
    Imagen_1 = Column(String(250), nullable=False)
    Opciones_1 = Column(String(250), nullable=False)
    Imagen_2 = Column(String(250), nullable=False)
    Opciones_2 = Column(String(250), nullable=False)
    Imagen_3 = Column(String(250), nullable=False)
    Opciones_3 = Column(String(250), nullable=False)

    juego_id = Column(Integer, ForeignKey("Juego.Id"))
    juego = relationship("Juegos", back_populates="opciones")
