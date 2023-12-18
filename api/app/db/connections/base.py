import os

from app.db.engines import Engine
from dotenv import load_dotenv
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session as Connection


class BaseConnection:
    def __init__(self) -> None:
        self.load_dotenv()
        self.engine = Engine(self.get_url())

    def get(self) -> Connection:
        return self.engine.get_connection()

    @staticmethod
    def load_dotenv() -> None:
        load_dotenv(dotenv_path=os.getenv("ENV_PATH_AND_FILENAME", ".env"))

    @staticmethod
    def get_url() -> URL:
        return URL.create(
            drivername="postgresql+pg8000",
        )
