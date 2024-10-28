import logging

import webview

from app.core.logger_setup import setup_logging
from app.controllers.main_controller import MainController

setup_logging()
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    api = MainController()
    window = webview.create_window("Rubaiyat", "app/templates/index.html", js_api=api)
    webview.start()
