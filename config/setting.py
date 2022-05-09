import os.path


class Config():
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path, 'data/cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_cases')

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # 日志文件路径
    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # config路径
    config_path = os.path.join(root_path, 'config')

    # yaml文件路径
    yaml_config_path = os.path.join(config_path, 'config.yaml')




class DevConfig(Config):
    #项目的域名
    host = 'http://127.0.0.1:8080/futureloan'


config = DevConfig()
