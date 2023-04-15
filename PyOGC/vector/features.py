from PyOGC.utils.helpers import get_query_data
from PyOGC.utils.urls import base_url


def get_collection_items(
    collection_id,
    bbox=None,
    subset=None,
    datetime=None,
    limit=10,
    result_type="results",
    property_name=None,
    filter=None,
    filter_lang=None,
    filter_crs=None,
    f=None,
):
    # Construct the URL
    url = f"{base_url}/collections/{collection_id}/items"

    # Construct the query parameters
    params = {}
    if bbox:
        params["bbox"] = ",".join(str(x) for x in bbox)
    if subset:
        params["subset"] = ",".join(subset)
    if datetime:
        params["datetime"] = datetime
    params["limit"] = limit
    params["resultType"] = result_type
    if property_name:
        params["propertyName"] = ",".join(property_name)
    if filter:
        params["filter"] = filter
    if filter_lang:
        params["filter-lang"] = filter_lang
    if filter_crs:
        params["filter-crs"] = filter_crs
    if f:
        params["f"] = f

    # Make the request using the get_query_data() function
    response = get_query_data(url, queries=params, response_format=f)

    # Return the JSON response
    return response
