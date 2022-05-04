import requests


class RequestHandler(object):
    def __init__(self):
        self.session = requests.Session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        res = self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)
        try:
            return res.json()
        except ValueError:
            print('not json')

    def close_session(self):
        self.session.close()