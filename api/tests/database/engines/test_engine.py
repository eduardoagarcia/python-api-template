from app.db.engines import Engine
from sqlalchemy.engine import URL
from sqlalchemy.orm.session import Session as Connection


class TestEngine:
    def setup_class(self) -> None:
        self.url: URL = URL.create(
            drivername="postgresql+pg8000",
            host="host.com",
            database="database",
            username="username",
            password="password",
            port=12345,
        )
        self.engine: Engine = Engine(self.url)

    def test_get_connection(self) -> None:
        connection = self.engine.get_connection()

        assert connection
        assert isinstance(connection, Connection)
