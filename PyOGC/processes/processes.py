from PyOGC.utils.helpers import get_data, post_data
from PyOGC.utils.urls import base_url


class ProcessesAPI:
    def get_processes(self, response_format="json"):
        url = f"{base_url}/processes"
        data = get_data(url, response_format)
        return data

    def get_process_description(self, process_id, response_format="json"):
        url = f"{base_url}/processes/{process_id}"
        data = get_data(url, response_format)
        return data

    def submit_workflow(self, process_id, data, response_format="json"):
        url = f"{base_url}/processes/{process_id}"
        response = post_data(url, data, response_format)
        return response

    def execute_workflow(self, process_id, data, response_format="json"):
        url = f"{base_url}/processes/{process_id}/execution"
        response = post_data(url, data, response_format)
        return response
