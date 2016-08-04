from recombee_api_client.api_requests.request import Request

class AddDetailView(Request):
    """
    Adds a detail view of a given item made by a given user.

    """

    def __init__(self,user_id, item_id, optional = dict()):
        """
        Required parameters:
        @param user_id: User who viewed the item
        
        @param item_id: Viewed item
        
        
        Optional parameters (given as dictionary C{optional}):
        @param timestamp: UTC timestamp of the view as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param duration: Duration of the view
        
        @param cascadeCreate: Sets whether the given user/item should be created if not present in the database.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = optional.get('timestamp')
        self.duration = optional.get('duration')
        self.cascade_create = optional.get('cascadeCreate')
        for par in optional:
            if not par in {"timestamp","duration","cascadeCreate"}:
                raise ValueError("Unknown parameter %s was given to the request" % par)
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/{databaseId}/detailviews/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        if self.timestamp is not None:
            p['timestamp'] = self.timestamp
        if self.duration is not None:
            p['duration'] = self.duration
        if self.cascade_create is not None:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params