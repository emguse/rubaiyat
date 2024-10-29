import logging
import logging.config
from pathlib import Path

import yaml


def setup_logging(default_path="logging.conf", default_level=logging.INFO) -> None:
    """Setup logging configuration"""
    path = Path(__file__).parent.parent.parent / default_path
    log_path = Path(__file__).parent.parent.parent / "logs/rubaiyat.log"

    # Ensure the logs directory exists
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(__name__)

    if path.exists():
        try:
            with open(path, "r") as f:
                config = yaml.safe_load(f)
                logging.config.dictConfig(config)
            logger.info(f"Logging configuration loaded from {path}")
        except Exception as e:
            logger.error(f"Failed to load logging configuration from {path}: {e}")
            logging.basicConfig(level=default_level)
            logger.info("Default logging configuration has been applied")
    else:
        logging.basicConfig(level=default_level)
        logger.warning(
            f"Logging configuration file not found at {path}. Using default logging settings."
        )
