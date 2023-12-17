from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes.v1 import hello
from .utils.consts import API


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()

    app.include_router(hello.hello_router, prefix=API.PREFIX + API.V1, tags=["Hello"])

    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health-check", status_code=200, tags=["Public"])
    async def app_health_check() -> dict[str, str]:
        return {"message": "Ok"}

    return app


api = create_app()
