import os

from app.db.connections.postgres import (
    PostgresConnection,
    postgres_connection,
)
from sqlalchemy.engine import URL
from sqlalchemy.orm.session import Session as Connection


class TestServiceConnection:
    def setup_class(self) -> None:
        self.service_connection = PostgresConnection()
        os.environ["POSTGRES_HOST"] = "host"
        os.environ["POSTGRES_DB"] = "database"
        os.environ["POSTGRES_USER"] = "user"
        os.environ["POSTGRES_PASSWORD"] = "***"
        os.environ["POSTGRES_PORT"] = "1234"

    def test_connection_get(self) -> None:
        connection = self.service_connection.get()

        assert connection
        assert isinstance(connection, Connection)

    def test_connection_get_url(self) -> None:
        url: URL = PostgresConnection.get_url()

        assert url
        assert isinstance(url, URL)

    def test_connection_get_local_url(self) -> None:
        url: str = PostgresConnection.get_url().__str__()
        expected = (
            "postgresql+pg8000://"
            + os.environ["POSTGRES_USER"]
            + ":"
            + os.environ["POSTGRES_PASSWORD"]
            + "@"
            + os.environ["POSTGRES_HOST"]
            + ":"
            + os.environ["POSTGRES_PORT"]
            + "/"
            + os.environ["POSTGRES_DB"]
        )

        assert url == expected

    def test_service_connection(self) -> None:
        assert postgres_connection()
        assert next(postgres_connection())
