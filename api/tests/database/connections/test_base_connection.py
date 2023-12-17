from app.db.connections.base import BaseConnection
from sqlalchemy.engine import URL
from sqlalchemy.orm.session import Session as Connection


class TestBaseConnection:
    def setup_class(self) -> None:
        self.base_connection = BaseConnection()

    def test_connection_get(self) -> None:
        connection = self.base_connection.get()

        assert connection
        assert isinstance(connection, Connection)

    def test_connection_get_url(self) -> None:
        url = BaseConnection.get_url()

        assert url
        assert isinstance(url, URL)
