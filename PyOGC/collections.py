from typing import Optional
from PyOGC.utils.helpers import get_data_collections
from PyOGC.utils.urls import base_url


def get_collections(
        datetime: Optional[str] = None,
        limit: Optional[int] = 10000,
        f: str = "json") -> dict:
    endpoint = f"{base_url}/collections"
    params = {}
    if datetime:
        params["datetime"] = datetime
    if limit:
        params["limit"] = limit
    data = get_data_collections(
        endpoint, datetime=datetime, limit=limit, response_format=f
    )
    return data
