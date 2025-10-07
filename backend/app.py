import os
from fastapi import FastAPI
from .routers import juego, usuario
from fastapi.responses import FileResponse
from .db.db import Base, engine
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(juego.router)
""" app.include_router(usuario.router) """

Base.metadata.create_all(bind = engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "..", "frontend", "template/index.html")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/", tags=["Home"])
def home():
    return FileResponse(INDEX_PATH)