import json
import unittest


from common.excel_handler import ExcelHandler
from common.logger_handler import LoggerHandler
from common.yaml_handler import YamlConfig
from config.setting import config
from common.requests_handler import RequestHandler
from libs import ddt


my_yaml = YamlConfig()
data = my_yaml.read_yaml(config.yaml_config_path)
logger_name = data['logger']['name']
logger_level = data['logger']['level']
logger_file = data['logger']['file']


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    logger = LoggerHandler(logger_name, logger_level, logger_file)

    def setUp(self) -> None:
        self.req = RequestHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register_success(self, test_data):
        print(test_data)
        # 访问接口 得到实际返回
        res = self.req.visit(test_data['method'],
                                    config.host + test_data['url'],
                                    json=json.loads(test_data['data']),
                                    headers=json.loads(test_data['headers']))
        try:
            self.assertEqual(test_data['expected'], res['code'])
        except AssertionError as e:
            self.logger.error('测试用例失败', e)

        # 对于断言失败的用例，将失败的用例保存到logger中






