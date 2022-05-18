from common.requests_handler import RequestHandler
from common.yaml_handler import yaml_data
from config.setting import config


def login():
    """ 登录，返回的是token"""
    req = RequestHandler()
    res = req.visit('post', config.host + '/member/login',
              json=yaml_data['user'], headers={"X-Media-Type": "v2"})
    return res


def save():
    pass


if __name__ == '__main__':
    print(login())

"""
jsonpath的用法
"""
