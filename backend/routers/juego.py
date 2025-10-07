from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.db import SessionLocal
from ..models.models import Juegos, Opciones
from ..schemas.schemas import JuegoCreate, JuegoOut, JuegoUpdate

router = APIRouter(prefix="/juego", tags=["Juego"])

# Dependencia: obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[JuegoOut])
async def obtener_juegos(db: Session = Depends(get_db)):
    juegos = db.query(Juegos).all()
    return juegos


@router.get("/{id}", response_model=JuegoOut)
async def obtener_juego(id: int, db: Session = Depends(get_db)):
    juego = db.query(Juegos).filter(Juegos.Id == id).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return juego


@router.post("/", response_model=JuegoOut, status_code=status.HTTP_201_CREATED)
async def crear_juego(juego: JuegoCreate, db: Session = Depends(get_db)):
    nuevo_juego = Juegos(Audio=juego.Audio, Nombre=juego.Nombre)
    db.add(nuevo_juego)
    db.commit()
    db.refresh(nuevo_juego)
    return nuevo_juego


@router.put("/{id}", response_model=JuegoOut)
async def actualizar_juego(id: int, juego: JuegoUpdate, db: Session = Depends(get_db)):
    juego_db = db.query(Juegos).filter(Juegos.Id == id).first()
    if not juego_db:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    juego_db.Audio = juego.Audio
    juego_db.Nombre = juego.Nombre
    db.commit()
    db.refresh(juego_db)
    return juego_db



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_juego(id: int, db: Session = Depends(get_db)):
    juego_db = db.query(Juegos).filter(Juegos.Id == id).first()
    if not juego_db:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    db.delete(juego_db)
    db.commit()
    return {"mensaje": f"Juego con ID {id} eliminado correctamente"}
