from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session as Connection
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Base = declarative_base()


class Engine:
    def __init__(self, connection_url: URL) -> None:
        engine = create_engine(connection_url)
        session = scoped_session(sessionmaker(bind=engine))
        self.connection = session()

    def get_connection(self) -> Connection:
        return self.connection
