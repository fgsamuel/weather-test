import requests


class ClientBase:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method, data=None, params=None, **kwargs):
        url = self.base_url
        response = self.session.request(method, url, data=data, params=params, **kwargs)
        response.raise_for_status()
        return response
