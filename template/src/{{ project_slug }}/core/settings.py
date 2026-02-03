from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Load environment variables as settings."""

    # Define environment variables of the project here
    ENVIRONMENT: Literal["local", "dev", "preprod", "prod"] = "local"

    # Load dotenv
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Avoid loading at every import
@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
