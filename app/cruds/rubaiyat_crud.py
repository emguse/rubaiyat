import csv
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

from sqlalchemy import text, func
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, select

from app.core.config import settings
from app.core.db import get_db
from app.models.rubaiyat_models import Rubaiyat

logger = logging.getLogger(__name__)


class RubaiyatRead:
    def __init__(self):
        self.engine = get_db()

    def read_from_id(self, id: int):
        try:
            with Session(self.engine) as session:
                statement = select(Rubaiyat).where(Rubaiyat.id == id)
                results = session.exec(statement).all()
                logger.info(f"Successfully read {len(results)} records from the database.")
                return results
        except Exception as e:
            logger.error(f"An error occurred while reading the record: {e}")
            raise

    def read_from_boozeism(self):
        try:
            with Session(self.engine) as session:
                statement = select(Rubaiyat).where(Rubaiyat.is_boozeism == True).order_by(func.random()).limit(1)
                randam_record = session.exec(statement).first()
                logger.info("Successfully read 1 records from the database.")
                return randam_record
        except Exception as e:
            logger.error(f"An error occurred while reading the record: {e}")
            raise


class RubaiyatCsv:
    def __init__(self, csv_path: Path):
        self.csv_path = csv_path
        self.json_data: List[Dict[str, Any]] = []
        self.engine = get_db()

    def import_csv(self) -> None:
        """
        Reads a CSV file from the specified path and converts it into JSON format.
        """
        logger.info(f"Starting to import CSV from {self.csv_path}")
        try:
            with open(self.csv_path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                self.json_data = [row for row in reader]  # Read as a list of dict

            # For confirmation after loading CSV
            logger.info(f"CSV file {self.csv_path} imported successfully with {len(self.json_data)} records.")
            logger.debug(json.dumps(self.json_data, indent=4, ensure_ascii=False))  # for DEBUG
        except FileNotFoundError as e:
            logger.error(f"CSV file not found: {self.csv_path} - {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to import CSV: {e}")
            raise

    def insert_into_db(self) -> None:
        """
        Inserts the JSON data into the Rubaiyat database table.
        """
        logger.info("Starting to insert data into the database.")
        try:
            with Session(self.engine) as session:
                for row in self.json_data:
                    rubaiyat_entry = Rubaiyat(
                        id=int(row["id"]),
                        is_with_parentheses=bool(int(row["is_with_parentheses"])),
                        section=row["section"],
                        poem_body=row["poem_body"],
                        poem_body_with_ruby=row["poem_body_with_ruby"],
                        is_boozeism=bool(int(row["is_boozeism"])),
                        footnote=row["footnote"] if row["footnote"] else None,
                    )
                    session.add(rubaiyat_entry)
                session.commit()
                logger.info(f"Successfully inserted {len(self.json_data)} records into the database.")
        except SQLAlchemyError as e:
            logger.error(f"Database insertion failed: {e}")
            session.rollback()
            raise
        except Exception as e:
            logger.error(f"An error occurred during database insertion: {e}")
            raise

    def truncate_tables(self) -> None:
        """
        Delete all records from the yourtag and Rubaiyat tables.
        Be careful, this method will erase all existing records in the table.
        """
        logger.info("Starting to delete all records from the yourtag and Rubaiyat tables.")
        try:
            with Session(self.engine) as session:
                session.exec(text("DELETE FROM yourtag"))
                session.exec(text("DELETE FROM rubaiyat"))
                session.commit()

                logger.info("All records from yourtag and Rubaiyat tables deleted successfully.")
        except SQLAlchemyError as e:
            logger.error(f"Failed to delete records from yourtag and Rubaiyat tables: {e}")
            session.rollback()
            raise


def import_rubaiyat_csv(csv_path: Path):
    """
    Write the data read from the CSV file into a database table.
    Be careful, this will erase all existing records in the table.
    """
    rubaiyat_csv = RubaiyatCsv(csv_path)
    rubaiyat_csv.truncate_tables()
    rubaiyat_csv.import_csv()
    rubaiyat_csv.insert_into_db()


if __name__ == "__main__":
    pass
