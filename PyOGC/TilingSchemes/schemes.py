from PyOGC.utils.helpers import get_data
from PyOGC.utils.urls import base_url


class TilesAPI:
    def get_tile_matrix_sets(self, response_format="json"):
        url = f"{base_url}/tileMatrixSets"
        data = get_data(url, response_format)
        return data

    def get_tile_matrix_set(self, tile_matrix_set_id, response_format="json"):
        url = f"{base_url}/tileMatrixSets/{tile_matrix_set_id}"
        data = get_data(url, response_format)
        return data
