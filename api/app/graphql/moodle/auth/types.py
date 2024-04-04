from typing import Optional

import strawberry
from pydantic import BaseModel


class MoodleLoginResponseModel(BaseModel):
    token: Optional[str] = None
    privatetoken: Optional[str] = None


@strawberry.experimental.pydantic.type(model=MoodleLoginResponseModel, all_fields=True)
class MoodleLoginResponse:
    pass
