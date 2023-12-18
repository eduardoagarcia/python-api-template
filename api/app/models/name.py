from typing import Optional, List

from app.db.engines import Base
from pydantic import BaseModel, PositiveInt
from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import Session as Connection


class Name(BaseModel):
    id: PositiveInt
    name: str = ""


class NameModel(Base):
    __tablename__ = "names"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)


class NameRepository:
    def __init__(self, connection: Connection) -> None:
        self.connection: Connection = connection

    def get_names(self) -> List[NameModel]:
        return self.connection.query(NameModel).order_by(NameModel.id.asc()).all()

    def get_by_id(self, name_id: BigInteger) -> Optional[NameModel]:
        if name := self.connection.query(NameModel).filter(NameModel.id == name_id).first():
            return name
        else:
            return None

    def create(self, name: str) -> NameModel:
        name = NameModel(
            name=name,
        )

        self.connection.add(name)
        self.connection.commit()
        return name

    def update(self, name_id: BigInteger, new_name: str) -> Optional[NameModel]:
        if name := self.connection.query(NameModel).filter(NameModel.id == name_id).first():
            name.name = new_name
            self.connection.commit()
            return name
        else:
            return None
