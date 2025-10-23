from typing import List
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    # Configuración general
    app_name: str
    debug: bool

    # Base de datos
    database_url: str
    database_url_sync: str

    # Seguridad
    secret_key: str
    algorithm: str

    # CORS
    allowed_origins: List[str]  
    

    class Config:
        env_file = BASE_DIR / ".env"

        
settings = Settings()
