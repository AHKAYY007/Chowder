from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite+aiosqlite:///./chowder.db"  # Use async SQLite driver for SQLAlchemy async engine

    # AI
    groq_api_key: Optional[str] = None
    groq_model: str = "llama3-8b-8192"  # Free model on Groq

    # Kite
    kite_rpc_url: str = "https://rpc-testnet.gokite.ai"
    kite_bundler_url: str = "https://bundler-service.staging.gokite.ai/rpc/"
    kite_chain_id: int = 2367  # Testnet, adjust for mainnet
    kite_private_key: Optional[str] = None
    kite_logger_address: Optional[str] = None

    # App
    app_name: str = "Chowder API"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()