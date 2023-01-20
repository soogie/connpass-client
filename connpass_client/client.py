import json
from urllib import parse, request


class ConnpassClient:
    def create_request(self, **kwargs) -> request.Request:
        query = {k:v for k,v in kwargs.items() if v is not None}
        url = parse.urlunparse(
            (
                "https",
                "connpass.com",
                "api/v1/event",
                None,
                parse.urlencode(query),
                None,
            )
        )
        return request.Request(url)

    
    def get(self, **kwargs) -> dict:
        req = self.create_request(**kwargs)
        with request.urlopen(req) as res:
            data = json.load(res)
        return data