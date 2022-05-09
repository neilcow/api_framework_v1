from common.requests_handler import RequestHandler


def login():
    """ 登录，返回的是token"""
    req = RequestHandler()
    req.visit()