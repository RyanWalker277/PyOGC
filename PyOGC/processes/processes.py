from PyOGC.utils.helpers import get_data, post_data
from PyOGC.utils.urls import base_url

class ProcessesAPI:

    def get_processes(self, response_format="json"):
        """
        Returns a list of available processes.
        """
        url = f"{base_url}/processes"
        data = get_data(url, response_format)
        return data

    def get_process_description(self, process_id, response_format="json"):
        """
        Returns the description of the process with the specified ID.
        """
        url = f"{base_url}/processes/{process_id}"
        data = get_data(url, response_format)
        return data
    
    def submit_workflow(self, process_id, data, response_format="json"):
        """
        Submit a processing workflow for execution and retrieve the virtual geospatial data resource.

        Args:
            process_id (str): The ID of the processing workflow.
            data (dict): The data to send with the POST request.
            response_format (str): The format in which to retrieve the data. Accepted values
                are 'json' or 'html'.

        Returns:
            dict: The virtual geospatial data resource, including links to resources supporting
                GET methods for all supported execution/output retrieval mechanisms.
        """
        url = f"{base_url}/processes/{process_id}"
        response = post_data(url, data, response_format)
        return response

    def execute_workflow(self, process_id, data, response_format="json"):
        """
        Execute a processing workflow synchronously.

        Args:
            process_id (str): The ID of the processing workflow.
            data (dict): The data to send with the POST request.
            response_format (str): The format in which to retrieve the data. Accepted values
                are 'json' or 'html'.

        Returns:
            dict: The execution output.
        """
        url = f"{base_url}/processes/{process_id}/execution"
        response = post_data(url, data, response_format)
        return response