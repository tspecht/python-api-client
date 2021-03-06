from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class AddPurchase(Request):
    """
    Adds a purchase of a given item made by a given user.

    """

    def __init__(self, user_id, item_id, timestamp=DEFAULT, cascade_create=DEFAULT):
        """
        Required parameters:
        @param user_id: User who purchased the item
        
        @param item_id: Purchased item
        
        
        Optional parameters:
        @param timestamp: UTC timestamp of the purchase as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param cascade_create: Sets whether the given user/item should be created if not present in the database.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/purchases/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        if self.timestamp is not DEFAULT:
            p['timestamp'] = self.timestamp
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
