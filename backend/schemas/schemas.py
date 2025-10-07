# backend/models/juego_schema.py
from pydantic import BaseModel

class JuegoCreate(BaseModel):
    Audio: str
    Nombre: str

class JuegoUpdate(JuegoCreate):
    pass

class JuegoOut(JuegoCreate):
    Id: int
    class Config:
        orm_mode = True


class OpcionesCreate(BaseModel):
    Imagen_1: str
    Opciones_1: str
    Imagen_2: str
    Opciones_2: str
    Imagen_3: str
    Opciones_3: str

class OpcionesUpdate(OpcionesCreate):
    pass

class OpcionesOut(OpcionesCreate):
    Id: int
    class Config:
        orm_mode = True


class UsuarioBase(BaseModel):
    Nombre: str
    Email: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    Id: int
    class Config:
        orm_mode = True