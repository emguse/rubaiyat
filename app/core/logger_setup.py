import logging
import logging.config
import yaml
from pathlib import Path


def setup_logging(default_path="logging.conf", default_level=logging.INFO) -> None:
    """Setup logging configuration"""
    path = Path(__file__).parent.parent.parent / default_path

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
        logger.warning(f"Logging configuration file not found at {path}. Using default logging settings.")


setup_logging()
