from fastapi import APIRouter, status, HTTPException
""" from ..schemas.schemas import JuegoCreate,JuegoOut,JuegoUpdate,OpcionesCreate,OpcionesOut,Opcionesupdate
 """
router = APIRouter(prefix="/juego")

@router.get("/", tags=["Juego"], status_code=status.HTTP_200_OK)
async def juegos():
    return "juego" 

@router.get("/{id}", tags=["Juego"], status_code=status.HTTP_200_OK)
async def juego(id):
    return {'juegos':{id}}

@router.post("/", tags=["Juego"], status_code=status.HTTP_200_OK)
async def new_juego():
    return {"creada con exito"}

@router.put("/{id}" , tags=["Juego"], status_code=status.HTTP_200_OK)
async def update_juego(id):
    return {"actulizado": id}

@router.delete("/{id}", tags=["Juego"], status_code=status.HTTP_200_OK)
async def delete_juego(id):
    return {"eliminado": id}