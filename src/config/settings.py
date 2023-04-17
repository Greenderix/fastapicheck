from functools import lru_cache

from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.types import PositiveInt

__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    class Config:
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True


class Settings(_Settings):
    """Server settings.

    Formed from `.env` or `.env.dev`.
    """
    DATABASE_URL: str


@lru_cache()
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""
    return Settings(_env_file=find_dotenv(env_file))
