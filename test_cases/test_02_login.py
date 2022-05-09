from common.db_handler import DBhandler
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
class TestRecharge(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')

    logger = LoggerHandler(logger_name, logger_level, logger_file)

    def setUp(self) -> None:
        self.req = RequestHandler()
        self.db = DBhandler(host=yaml_data['database']['host'],
                            port=yaml_data['database']['port'],
                            user=yaml_data['database']['user'],
                            password=yaml_data['database']['password'],
                            database=yaml_data['database']['database'],
                            charset=yaml_data['database']['charset'])
        

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge_success(self, test_data):
        pass