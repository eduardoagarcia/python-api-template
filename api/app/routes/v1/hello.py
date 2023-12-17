from app.db.connections.postgres import postgres_connection
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session as Connection

hello_router: APIRouter = APIRouter(prefix="/hello")


@hello_router.get(
    "/world",
    response_model=dict[str, str]
)
def world(
        connection: Connection = Depends(postgres_connection),
) -> dict[str, str]:
    return {"message": "Hello World!"}
