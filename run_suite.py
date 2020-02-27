import time
import unittest

import app

from script.test_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLogin))
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb') as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="V1.0.0")
    # 使用Runner运行测试套件
    runner.run(suite)
