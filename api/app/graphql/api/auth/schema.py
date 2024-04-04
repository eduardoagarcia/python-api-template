import strawberry

from .api import api_login
from .types import APILoginResponse, APILoginResponseModel


async def login(username: str, password: str) -> APILoginResponse:
    api_login_response: APILoginResponseModel = await api_login(username=username, password=password)

    return APILoginResponse.from_pydantic(api_login_response)


@strawberry.type
class APIAuthOperations:
    login: APILoginResponse = strawberry.field(resolver=login)
