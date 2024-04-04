import strawberry

from .api import moodle_login
from .types import MoodleLoginResponse, MoodleLoginResponseModel


async def login(username: str, password: str) -> MoodleLoginResponse:
    moodle_login_response: MoodleLoginResponseModel = await moodle_login(username=username, password=password)

    return MoodleLoginResponse.from_pydantic(moodle_login_response)


@strawberry.type
class MoodleAuthOperations:
    login: MoodleLoginResponse = strawberry.field(resolver=login)
