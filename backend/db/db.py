from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

data =(

)

conn_str = (
    

)

engine = create_engine(conn_str)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()