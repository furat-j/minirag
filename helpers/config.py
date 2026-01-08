#
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    APP_NAME: str = "mini-RAG"
    APP_VERSION: str = "0.1.0"
    OPENAI_API_KEY: str = ""
    FILE_ALLOWED_TYPES: list[str] = ["text/plain", "application/pdf"]
    FILE_MAX_SIZE: int = 10_485_760
    FILE_DEFAULT_CHUNK_SIZE: int = 512_000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @field_validator('FILE_ALLOWED_TYPES', mode='before')
    @classmethod
    def parse_allowed_types(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.split(",")]
        return v


def get_settings() -> Settings:
    return Settings()