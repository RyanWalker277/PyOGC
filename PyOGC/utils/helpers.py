import requests

def get_data(endpoint: str, response_format: str) -> str:
    """
    Retrieves data from an endpoint in the specified format.

    Args:
        endpoint (str): The URL endpoint to retrieve data from.
        response_format (str): The format in which to retrieve the data. Accepted values
            are 'json' or 'html'.

    Returns:
        str: The retrieved data.

    Raises:
        ValueError: If an invalid format is specified.
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    headers = {"accept": f"application/{response_format}"}

    try:
        if response_format == "json":
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        elif response_format == "html":
            html_endpoint = f"{endpoint}&f=html" if "?" in endpoint else f"{endpoint}?f=html"
            response = requests.get(html_endpoint)
            response.raise_for_status()
            return response.text
        elif response_format == "econ":
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.content.decode()
        else:
            raise ValueError(f"Invalid format specified: {response_format}")
    except requests.exceptions.RequestException as e:
        raise e

import requests

def get_data_collections(endpoint, response_format, datetime=None, limit=None):
    """
    Sends a GET request to the specified endpoint and returns the data in the
    specified response format. Supports the /collections endpoint with optional
    datetime and limit parameters.
    
    :param endpoint: The URL to send the request to.
    :type endpoint: str
    :param response_format: The format of the response. Accepted values are 'json', 'html', or 'econ'.
    :type response_format: str
    :param datetime: Optional datetime or interval string to filter the collections by.
    :type datetime: str or None
    :param limit: Optional limit on the number of collections to return.
    :type limit: int or None
    
    :return: The data returned by the API.
    :rtype: dict or str
    :raises ValueError: If an invalid response format is specified.
    :raises requests.exceptions.RequestException: If there was an error making the request.
    """
    headers = {"Accept": f"application/{response_format}"}
    if datetime is not None:
        endpoint += f"?datetime={datetime}"
    if limit is not None:
        endpoint += f"&limit={limit}"
    
    try:
        if response_format == "json":
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        elif response_format == "html":
            html_endpoint = f"{endpoint}&f=html" if "?" in endpoint else f"{endpoint}?f=html"
            response = requests.get(html_endpoint)
            response.raise_for_status()
            return response.text
        elif response_format == "econ":
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.content
        else:
            raise ValueError(f"Invalid format specified: {response_format}")
    except requests.exceptions.RequestException as e:
        raise e
