import http
import os
from typing import Optional

import requests
from dotenv import load_dotenv
from pydantic import BaseModel

from app.graphql.moodle.api import generate_moodle_url

load_dotenv()


class MoodleLoginResponse(BaseModel):
    token: Optional[str] = None
    privatetoken: Optional[str] = None


def moodle_login(username: str, password: str) -> MoodleLoginResponse:
    empty_response: MoodleLoginResponse = MoodleLoginResponse(token="", privatetoken="")

    response = requests.get(
        generate_moodle_url(os.getenv("MOODLE_API_LOGIN_PATH")),
        params={
            "username": username,
            "password": password,
            "service": os.getenv("MOODLE_WEB_SERVICE"),
        },
    )

    if response.status_code == http.HTTPStatus.OK:
        if "error" not in response.json():
            return MoodleLoginResponse(**response.json())
        else:
            return empty_response
    else:
        return empty_response
