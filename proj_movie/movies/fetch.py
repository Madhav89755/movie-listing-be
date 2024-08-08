from django.conf import settings
import requests
import base64

credentials = f'{settings.API_USERNAME}:{settings.API_PASSWORD}'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {encoded_credentials}',
    "User-Agent":"Thunder Client (https://www.thunderclient.com)",
    "Accept":"*/*"
}

def fetch_movies(page=None):
    if page:
        page=f'page={page}'
    response = requests.get(f"{settings.API_URL}?{page or ''}", headers=headers, verify=False)
    return response.status_code, response.json()
