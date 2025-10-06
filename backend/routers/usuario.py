from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix="/usuarios")

@router.get("/", tags=["Usuarios"], status_code=status.HTTP_200_OK)
async def usuarios():
    return "mira usuarios"

@router.get("/{id}", tags=["Usuarios"], status_code=status.HTTP_200_OK)
async def usuario(id):
    return {"un usuario"+id}

@router.post("/", tags=["Usuarios"], status_code=status.HTTP_200_OK)
async def new_user():
    return "usuarios"

@router.put("/{id}", tags=["Usuarios"], status_code=status.HTTP_200_OK)
async def update_user(id):
    return {"user":id}

@router.delete("/{id}", tags=["Usuarios"], status_code=status.HTTP_200_OK)
async def delete_user(id):
    return {"user": id}