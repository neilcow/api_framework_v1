import os
import unittest
# 1、初始化testloader
from libs.HTMLTestRunnerNew import HTMLTestRunner
import time
from config.setting import config


testloader = unittest.TestLoader()

# 2、 查找测试用例，加载

suite = testloader.discover(config.case_path)

print(suite)

# 生成report

# file_path = os.path.join(report_path, 'test_result.txt')

ti = str(int(time.time()))
file_name = 'test_result_{}.html'.format(ti)

file_path = os.path.join(config.report_path, file_name)

# text ,对于html 一定要用二进制形式打开，wb
with open(file_path, 'wb') as f:
    # 初始化运行期，是以普通文本生成测试报告，TextTestRunner
    # runner = unittest.TextTestRunner(f, verbosity=2)
    runner = HTMLTestRunner(f,
                            title="测试报告",
                            description='测试报告描述')
    runner.run(suite)

