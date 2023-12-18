from typing import List

from app.db.connections.postgres import postgres_connection
from app.models.name import NameRepository, Name
from fastapi import APIRouter, Depends, HTTPException
from pydantic import PositiveInt
from sqlalchemy.orm import Session as Connection

hello_router: APIRouter = APIRouter(prefix="/hello")


@hello_router.get("/world", response_model=dict[str, str])
def world() -> dict[str, str]:
    return {"message": "Hello World!"}


@hello_router.get("/names", response_model=List[Name])
def get_names(
        connection: Connection = Depends(postgres_connection)
) -> List[Name]:
    name_repo = NameRepository(connection)
    return name_repo.get_names()


@hello_router.get("/name", response_model=Name)
def get_name(
        id: PositiveInt,
        connection: Connection = Depends(postgres_connection)
) -> Name:
    name_repo = NameRepository(connection)
    name_model = name_repo.get_by_id(name_id=id)

    if name_model is None:
        raise HTTPException(status_code=404, detail="Name not found")

    return name_model


@hello_router.post("/name", response_model=Name)
def create_name(
        name: str = None,
        connection: Connection = Depends(postgres_connection)
) -> Name:
    if name is None:
        raise HTTPException(status_code=400, detail="Invalid parameters")

    name_repo = NameRepository(connection)
    name_model = name_repo.create(name=name)

    if name_model is None:
        raise HTTPException(status_code=404, detail="Name not found")

    return name_model


@hello_router.put("/name", response_model=Name)
def update_name(
        id: PositiveInt = None,
        name: str = None,
        connection: Connection = Depends(postgres_connection)
) -> Name:
    if id is None or name is None:
        raise HTTPException(status_code=400, detail="Invalid parameters")

    name_repo = NameRepository(connection)
    name_model = name_repo.update(name_id=id, new_name=name)

    if name_model is None:
        raise HTTPException(status_code=404, detail="Name not found")

    return name_model
