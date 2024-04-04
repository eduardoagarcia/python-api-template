import os

from dotenv import load_dotenv

load_dotenv()


def generate_api_url(path: str) -> str:
    return "/".join([os.getenv("API_URL").rstrip("/"), path.lstrip("/")])
