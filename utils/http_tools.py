
import requests
from requests.exceptions import RequestException

def simple_get(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except RequestException as e:
        return f"Request failed: {str(e)}"

def get_http_headers(url):
    try:
        response = requests.head(url, timeout=10)
        response.raise_for_status()
        return response.headers
    except RequestException as e:
        return f"Request failed: {str(e)}"
