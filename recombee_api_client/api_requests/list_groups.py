from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class ListGroups(Request):
    """
    Gets the list of all the groups currently present in the database.
    """

    def __init__(self):
        """
        """
        self.timeout = 239000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/groups/list/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
