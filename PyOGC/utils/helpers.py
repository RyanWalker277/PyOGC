import requests


def get_data(endpoint: str, response_format: str) -> str:
    headers = {"accept": f"application/{response_format}"}

    try:
        if response_format == "json":
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        elif response_format == "html":
            html_endpoint = (
                f"{endpoint}&f=html" if "?" in endpoint else
                f"{endpoint}?f=html")
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


def get_data_collections(endpoint, response_format, datetime=None, limit=None):
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
            html_endpoint = (
                f"{endpoint}&f=html" if "?" in endpoint else
                f"{endpoint}?f=html")
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


def get_query_data(endpoint: str, response_format: str, queries: dict) -> str:
    headers = {"accept": f"application/{response_format}"}
    query_string = "&".join(
        [f"{key}={value}" for key, value in queries.items()])
    full_endpoint = f"{endpoint}?{query_string}"
    print(full_endpoint)

    try:
        if response_format == "json":
            response = requests.get(full_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        elif response_format == "html":
            html_endpoint = (
                f"{full_endpoint}&f=html"
                if "?" in full_endpoint
                else f"{full_endpoint}?f=html"
            )
            response = requests.get(html_endpoint)
            response.raise_for_status()
            return response.text
        elif response_format == "econ":
            response = requests.get(full_endpoint, headers=headers)
            response.raise_for_status()
            return response.content.decode()
        else:
            raise ValueError(f"Invalid format specified: {response_format}")
    except requests.exceptions.RequestException as e:
        raise e


def post_data(endpoint: str, data: dict, response_format: str) -> str:
    headers = {"accept": f"application/{response_format}"}

    try:
        if response_format == "json":
            response = requests.post(endpoint, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        elif response_format == "html":
            response = requests.post(endpoint, data=data, headers=headers)
            response.raise_for_status()
            return response.text
        else:
            raise ValueError(f"Invalid format specified: {response_format}")
    except requests.exceptions.RequestException as e:
        raise e
