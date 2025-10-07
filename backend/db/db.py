from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Datos de conexión (ajústalos con tus credenciales)
USER = "root"
PASSWORD = "0000"
HOST = "localhost"
PORT = "3306"
DB_NAME = "juego_sonidos"

# Cadena de conexión
conn_str = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Crear el motor de conexión
engine = create_engine(conn_str, echo=True)

# Crear la sesión
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base para los modelos
Base = declarative_base()
