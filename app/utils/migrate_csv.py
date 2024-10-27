import logging
from pathlib import Path

import app.core.logger_setup as _
from app.core.config import settings
from app.cruds.rubaiyat_crud import import_rubaiyat_csv

logger = logging.getLogger(__name__)

DEFAULT_CSV_PATH = Path(settings.DEFAULT_CSV_PATH)


def run_migration(csv_path=DEFAULT_CSV_PATH) -> None:
    logger.info("Starting CSV to database migration...")

    try:
        import_rubaiyat_csv(csv_path)
        logger.info("Migration completed successfully.")
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()
