from app.db.connections.postgres import postgres_connection
from app.routes.v1.hello import hello_router
from app.utils.consts import API
from fastapi import FastAPI
from fastapi.testclient import TestClient
from http import HTTPStatus
from unittest.mock import Mock

app = FastAPI()
app.include_router(hello_router, prefix=API.PREFIX + API.V1)
client = TestClient(app, base_url="http://localhost")


class TestHelloRequestHandler:
    full_url_prefix = API.PREFIX + API.V1

    postgres_connection_mock = Mock()

    def override_postgres_connection(self) -> Mock:
        return self.postgres_connection_mock

    def test_get_hello(self) -> None:
        app.dependency_overrides[postgres_connection] = self.override_postgres_connection

        response = client.get(self.full_url_prefix + "/hello/world")

        assert response.status_code == HTTPStatus.OK
        response_json = response.json()
        assert response_json["message"] == "Hello World!"
