from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Load environment variables as settings."""

    # Define environment variables of the project here

    # ENVIRONMENT
    environment: Literal["local", "test", "dev", "preprod", "prod"] = "local"

    # LOG_LEVEL
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = (
        "INFO"
    )

    # Load dotenv
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Avoid loading at every import
@lru_cache
def get_settings() -> Settings:
    """Return settings"""
    return Settings()


settings = get_settings()
