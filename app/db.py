from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models_db import Base
from .config import settings 

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    # connect_args={"check_same_thread": False}  #* For SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()