from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    RABBIT_HOST: str = "localhost"
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()