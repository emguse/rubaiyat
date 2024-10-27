import logging
from alembic.config import Config
from alembic import command

import app.core.logger_setup as _

logger = logging.getLogger(__name__)


def run_alembic_upgrade():
    """
    Run the Alembic upgrade command to update database schema.
    """
    logger.info("Starting Alembic migration...")

    try:
        # Load the Alembic configuration file
        alembic_cfg = Config("alembic.ini")

        # Apply migrations (upgrade to latest version)
        command.upgrade(alembic_cfg, "head")
        logger.info("Alembic migration completed successfully.")
    except Exception as e:
        logger.error(f"Alembic migration failed: {e}")
        raise


if __name__ == "__main__":
    run_alembic_upgrade()
