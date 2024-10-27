import logging
from pathlib import Path
from typing import Generator

from sqlmodel import Session, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session as SessionType

from app.core.config import settings

logger = logging.getLogger(__name__)

sqlite_path = settings.SQLITE_FILE_PATH
sqlite_file_name = settings.SQLITE_FILE_NAME
sqlite_url = "sqlite:///" + str(Path.joinpath(Path(settings.SQLITE_FILE_PATH), settings.SQLITE_FILE_NAME))

logger.info(f"SQLite database URL: {sqlite_url}")

try:
    engine: Engine = create_engine(sqlite_url, echo=False)
    logger.info("Database engine created successfully")
except Exception as e:
    logger.error(f"Failed to create database engine: {e}")
    raise


def get_db() -> Engine:
    return engine


def get_session() -> Generator[SessionType, None, None]:
    try:
        with Session(engine) as session:
            logger.debug("Session started successfully")
            yield session
    except Exception as e:
        logger.error(f"Failed to create session: {e}")
        raise


def init_db() -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # SQLModel.metadata.create_all(engine)
    logger.info("Database initialization skipped because Alembic is handling migrations")
