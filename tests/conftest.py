import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base  
TEST_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(TEST_DATABASE_URL, echo=False)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()