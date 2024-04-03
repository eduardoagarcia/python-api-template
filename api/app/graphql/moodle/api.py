import http
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def generate_moodle_url(path: str) -> str:
    return "/".join([os.getenv("MOODLE_API_URL").rstrip("/"), path.lstrip("/")])


def moodle_api(function_name: str, params: object = None, token: str = None) -> object | None:
    if params is None:
        params = {}

    common_params = {
        "wsfunction": function_name,
        "moodlewsrestformat": "json",
        "wstoken": token
    }

    response = requests.get(generate_moodle_url(os.getenv("MOODLE_API_PATH")), params={**common_params, **params})

    if response.status_code == http.HTTPStatus.OK:
        return response.json()
    else:
        return None
