from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AutoBackend"

    # Database
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/autobackend"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"

    # OpenAI
    OPENAI_API_KEY: str = ""

    # Runtime
    MAX_AI_COST_PER_REQUEST: float = 1.0
    MAX_LOOPS: int = 3

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()