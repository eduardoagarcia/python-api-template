from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL

from .graphql import schema


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", status_code=200, tags=["Public"])
    async def app_health_check() -> dict[str, str]:
        return {"message": "Ok"}

    app.add_route("/graphql", GraphQL(schema))
    app.add_websocket_route("/graphql", GraphQL(schema))

    return app


api = create_app()
