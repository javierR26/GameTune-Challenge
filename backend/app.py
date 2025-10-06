import os
from fastapi import FastAPI
from .routers import juego, usuario
from fastapi.responses import FileResponse

app = FastAPI()
app.include_router(juego.router)
app.include_router(usuario.router)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "..", "frontend", "index.html")

@app.get("/", tags=["Home"])
def home():
    return FileResponse(INDEX_PATH)