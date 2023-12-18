from http import HTTPStatus
from unittest.mock import Mock

from app.db.connections.postgres import postgres_connection
from app.models.name import NameModel
from app.routes.v1.hello import hello_router
from app.utils.consts import API
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
app.include_router(hello_router, prefix=API.PREFIX + API.V1)
client = TestClient(app, base_url="http://localhost")


class TestHelloRequestHandler:
    full_url_prefix = API.PREFIX + API.V1

    postgres_connection_mock = Mock()

    def override_postgres_connection(self) -> Mock:
        return self.postgres_connection_mock

    def test_get_hello(self) -> None:
        response = client.get(self.full_url_prefix + "/hello/world")

        expected_response = {
            "message": "Hello World!"
        }
        assert response.status_code == HTTPStatus.OK
        assert response.json() == expected_response

    def test_get_nams(self) -> None:
        self.postgres_connection_mock.query().order_by().all.return_value = [
            NameModel(
                id=1,
                name="Test McTester"
            ),
            NameModel(
                id=2,
                name="Jest McJester"
            )
        ]
        app.dependency_overrides[postgres_connection] = self.override_postgres_connection

        response = client.get(self.full_url_prefix + "/hello/names")

        expected_response = [
            {"id": 1, "name": "Test McTester"},
            {"id": 2, "name": "Jest McJester"}
        ]
        assert response.status_code == HTTPStatus.OK
        assert response.json() == expected_response

    def test_get_name(self) -> None:
        self.postgres_connection_mock.query().filter().first.return_value = (
            NameModel(
                id=1,
                name="Test McTester"
            )
        )
        app.dependency_overrides[postgres_connection] = self.override_postgres_connection

        response = client.get(self.full_url_prefix + "/hello/name", params={"id": 1})

        expected_response = {
            "id": 1, "name": "Test McTester"
        }
        assert response.status_code == HTTPStatus.OK
        assert response.json() == expected_response
