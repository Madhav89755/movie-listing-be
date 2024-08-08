import requests
import base64
from django.conf import settings
from utils.logging import unknown_exception_logger
from utils.static_messages import API_RETRY_MAX_LIMIT_REACHED

credentials = f'{settings.API_USERNAME}:{settings.API_PASSWORD}'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {encoded_credentials}',
    "User-Agent":"Thunder Client (https://www.thunderclient.com)",
    "Accept":"*/*"
}

def fetch_movies(page:int=None, retry_limit:int=3)->tuple[bool|int, str|dict]:
    if retry_limit==0:
        print(API_RETRY_MAX_LIMIT_REACHED)
        print("======================================================")
        return False, API_RETRY_MAX_LIMIT_REACHED
    try:
        if page:
            page=f'page={page}'
        response = requests.get(f"{settings.API_URL}?{page or ''}", headers=headers, verify=False)
        return response.status_code, response.json()
    except Exception as e:
        print(f"Exception occurred for retry number {retry_limit}")
        unknown_exception_logger(e)
        retry_limit-=1
        fetch_movies(page, retry_limit)