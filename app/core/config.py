import logging
from pathlib import Path

from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / ".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    PROJECT_NAME: str
    SQLITE_FILE_PATH: Path
    SQLITE_FILE_NAME: str
    SQLITE_URL: str
    DEFAULT_CSV_PATH: Path

    @field_validator("SQLITE_FILE_PATH", mode="before")
    def convert_to_sqlite_path(cls, v) -> Path:
        if isinstance(v, str):
            logger.debug(f"Converting string to Path: {v}")
            return Path(v)
        logger.error("Invalid config value for SQLITE_FILE_PATH: not a string")
        raise ValueError("Invalid confg value: Type not string")

    @field_validator("DEFAULT_CSV_PATH", mode="before")
    def convert_to_csv_path(cls, v) -> Path:
        if isinstance(v, str):
            logger.debug(f"Converting string to Path: {v}")
            return Path(v)
        logger.error("Invalid config value for DEFAULT_CSV_PATH: not a string")
        raise ValueError("Invalid confg value: Type not string")


# Create and log a Settings instance
try:
    settings = Settings()
    logger.info(f"Settings loaded successfully: {settings.model_dump_json()}")
except Exception as e:
    logger.error(f"Failed to load settings: {str(e)}")
