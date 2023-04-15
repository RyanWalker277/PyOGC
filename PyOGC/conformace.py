from PyOGC.utils.helpers import get_data


def get_conformance(f="json"):
    endpoint = "https://maps.gnosis.earth/ogcapi/conformance"
    data = get_data(endpoint, f)
    return data
