import requests
from PyOGC.utils.helpers import get_data
from PyOGC.utils.urls import base_url


def metadata(f="html"):
    try:
        response = get_data(base_url, f)
        return response
    except requests.exceptions.RequestException as e:
        raise e
