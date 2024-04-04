import http
import os

import httpx
from dotenv import load_dotenv

from .types import APILoginResponseModel
from ..api import generate_api_url

load_dotenv()


async def api_login(username: str, password: str) -> APILoginResponseModel:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            generate_api_url(os.getenv("API_LOGIN_PATH")),
            json={
                "username": username,
                "password": password,
            },
        )

    if response.status_code == http.HTTPStatus.OK:
        return APILoginResponseModel(**response.json())
    else:
        raise Exception(f"API Login Error {response.status_code}: {response.text}")
