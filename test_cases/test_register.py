
import unittest

import ddt

from common.excel_handler import ExcelHandler
from config.setting import config
from common.requests_handler import RequestHandler


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    @ddt.data(*data)
    def test_register_success(self, test_data):
        print(test_data)
        # 访问接口 得到实际返回
        res = RequestHandler().visit(test_data['method'],
                                    config.host + test_data['url'],
                                    json=eval(test_data['data']),
                                    headers=eval(test_data['headers']))
        self.assertEqual(test_data['expected'], res['code'])
        






