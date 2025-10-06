from pydantic import BaseModel

class JuegoCreate(BaseModel):
    Audio: str
    Nombre : str

class JuegoUpdate(JuegoCreate):
    pass

class JuegoOut(JuegoCreate):
    Id: int
    class Config:
        orm_mode =True

class OpcionesCreate(BaseModel):
    Imagen_1 : str
    Opciones_1 : str
    Imagen_2 : str
    Opciones_2 : str
    Imagen_3 : str
    Opciones_3 : str

class Opcionesupdate(OpcionesCreate):
    pass

class OpcionesOut(OpcionesCreate):
    Id: int
    class Config:
        orm_mode = True