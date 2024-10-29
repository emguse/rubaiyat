import logging

import webview

from app.controllers.main_controller import MainController
from app.core.logger_setup import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    api = MainController()
    window = webview.create_window(
        title="Rubaiyat", url="templates/index.html", js_api=api
    )
    webview.start(gui="qt", debug=True)
