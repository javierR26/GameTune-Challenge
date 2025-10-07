""" from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.db import SessionLocal
from ..models.models import Usuarios
from ..schemas.schemas import UsuarioCreate, UsuarioOut, UsuarioUpdate

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Dependencia para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[UsuarioOut])
async def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuarios).all()
    return usuarios


@router.get("/{id}", response_model=UsuarioOut)
async def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.Id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuarios(Nombre=usuario.Nombre, Email=usuario.Email)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.put("/{id}", response_model=UsuarioOut)
async def actualizar_usuario(id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuarios).filter(Usuarios.Id == id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario_db.Nombre = usuario.Nombre
    usuario_db.Email = usuario.Email
    db.commit()
    db.refresh(usuario_db)
    return usuario_db


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuarios).filter(Usuarios.Id == id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario_db)
    db.commit()
    return {"mensaje": f"Usuario con ID {id} eliminado correctamente"}
 """