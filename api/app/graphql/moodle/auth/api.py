import http
import os

import httpx
from dotenv import load_dotenv

from .types import MoodleLoginResponseModel
from ..api import generate_moodle_url

load_dotenv()


async def moodle_login(username: str, password: str) -> MoodleLoginResponseModel:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            generate_moodle_url(os.getenv("MOODLE_API_LOGIN_PATH")),
            params={
                "username": username,
                "password": password,
                "service": os.getenv("MOODLE_WEB_SERVICE"),
            },
        )

    if response.status_code == http.HTTPStatus.OK:
        if "error" not in response.json():
            return MoodleLoginResponseModel(**response.json())
        else:
            raise Exception(response.json())
    else:
        raise Exception(f"Moodle Login Error {response.status_code}: {response.text}")
