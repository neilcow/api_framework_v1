import json
import unittest


from common.excel_handler import ExcelHandler
from common.helper import generate_mobile
from common.logger_handler import LoggerHandler
from common.yaml_handler import YamlConfig
from config.setting import config
from common.requests_handler import RequestHandler
from libs import ddt


my_yaml = YamlConfig()
yaml_data = my_yaml.read_yaml(config.yaml_config_path)
logger_name = yaml_data['logger']['name']
logger_level = yaml_data['logger']['level']
logger_file = yaml_data['logger']['file']


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

        if '#exist_phone#' in test_data['data']:
            # mobile = generate_mobile()

            # 从数据库里查询，如果数据库里有这个手机号，
            # 查询数据库，随机找一个，直接使用号码替换

            test_data['data'] = test_data['data'].replace('#exist_phone', mobile)

        if '#new_phone#' in test_data['data']:
            while True:
                mobile = generate_mobile()

                # 从数据库里查询，如果数据库里有这个手机号，
                # 查询数据库，随机找一个，直接使用号码替换

                test_data['data'] = test_data['data'].replace('#new_phone', mobile)
        try:
            self.assertEqual(test_data['expected'], res['code'])
            self.excel_handler.write(config.data_path, 'register', test_data['case_id']+1,
                                     10, '测试通过')
        except AssertionError as e:
            self.logger.error('测试用例失败:{}'.format(e))
            # 一定要手动抛出异常，否则测试用例会自动通过
            self.excel_handler.write(config.data_path, 'register', test_data['case_id'] + 1,
                                     10, '测试失败')
            raise e

        # 对于断言失败的用例，将失败的用例保存到logger中






