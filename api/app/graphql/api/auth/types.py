from datetime import datetime
from typing import Optional

import strawberry
from pydantic import BaseModel, HttpUrl


class APIUserModel(BaseModel):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    type: Optional[str] = None
    is_staff: bool
    birthday: Optional[datetime] = None
    avatar: HttpUrl
    company: Optional[str] = None
    position: Optional[str] = None
    contact_number: Optional[str] = None
    bio: Optional[str] = None


class APILoginResponseModel(BaseModel):
    token: str
    user: APIUserModel
    refresh_token: str
    first_login: bool
    token_exp_date: datetime
    type: Optional[str] = None


@strawberry.experimental.pydantic.type(model=APIUserModel, all_fields=True)
class APIUser:
    pass


@strawberry.experimental.pydantic.type(model=APILoginResponseModel, all_fields=True)
class APILoginResponse:
    pass
