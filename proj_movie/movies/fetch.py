import requests
import base64
from django.conf import settings
from utils.logging import unknown_exception_logger
from utils.static_messages import API_RETRY_MAX_LIMIT_REACHED

credentials = f'{settings.API_USERNAME}:{settings.API_PASSWORD}'
encoded_credentials = base64.b64encode(
    credentials.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {encoded_credentials}',
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Accept": "*/*"
}


def fetch_movies(page: int = None, retry_limit: int = 3) -> tuple[bool | int, str | dict]:
    for x in range(0,retry_limit):
        try:
            print(f"Movie API Hit #{x+1}")
            url=settings.API_URL
            if page:
                url = f'{url}?page={page}'
            resp = requests.get(
                f"{url}", headers=headers, verify=False)
            response=(resp.status_code, resp.json())
        except Exception as e:
            unknown_exception_logger(e)
            response=(404, API_RETRY_MAX_LIMIT_REACHED)
    return response