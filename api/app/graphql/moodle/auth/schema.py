from typing import Optional

import strawberry

from app.graphql.moodle.auth.api import moodle_login, MoodleLoginResponse


@strawberry.type
class LoginResponse:
    token: str
    private_token: Optional[str]


@strawberry.type
class AuthQuery:
    @strawberry.field
    def login(self, username: str, password: str) -> LoginResponse:
        login_response: MoodleLoginResponse = moodle_login(username=username, password=password)

        return LoginResponse(token=login_response.token, private_token=login_response.privatetoken)
