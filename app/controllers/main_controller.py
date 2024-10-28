import logging
import random

from app.cruds.rubaiyat_crud import RubaiyatRead

logger = logging.getLogger(__name__)


class MainController:
    def __init__(self):
        self.rubaiyat_read = RubaiyatRead()

    def random_rubaiyat(self):
        id = random.randint(1, 143)
        results = self.rubaiyat_read.read_from_id(id)
        results_json = [result.model_dump_json() for result in results]
        logger.info("Ramdom read success.")
        return results_json

    def random_rubaiyat_in_boozeism(self):
        results = self.rubaiyat_read.read_from_boozeism()
        results_json = [result.model_dump_json() for result in results]
        logger.info("Booze-ism ramdom read success.")
        return results_json


if __name__ == "__main__":
    pass
