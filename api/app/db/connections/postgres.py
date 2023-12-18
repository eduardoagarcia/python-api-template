import os
from typing import Iterator, Optional

from app.db.connections.base import BaseConnection
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session as Connection


class PostgresConnection(BaseConnection):
    @staticmethod
    def get_url() -> URL:
        port_str: Optional[str] = os.getenv("POSTGRES_PORT", None)
        port = int(port_str) if port_str is not None else None

        return URL.create(
            drivername="postgresql+pg8000",
            host=os.getenv("POSTGRES_HOST", None),
            database=os.getenv("POSTGRES_DB", None),
            username=os.getenv("POSTGRES_USER", None),
            password=os.getenv("POSTGRES_PASSWORD", None),
            port=port,
        )


def postgres_connection() -> Iterator[Connection]:
    connection: Connection = PostgresConnection().get()
    try:
        yield connection
    finally:
        connection.close()
