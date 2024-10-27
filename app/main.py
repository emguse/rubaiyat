import logging
import random

import app.core.logger_setup as _
from app.cruds.rubaiyat_crud import RubaiyatRead

logger = logging.getLogger(__name__)


def main():
    logger.info("Hello from rubaiyat!")
    id = random.randint(1, 143)
    rubaiyat = RubaiyatRead()
    results = rubaiyat.read_from_id(id)
    for row in results:
        print(row.id, row.poem_body)
    boozeism_results = rubaiyat.read_from_boozeism()
    print(boozeism_results.id, boozeism_results.poem_body)


if __name__ == "__main__":
    main()
