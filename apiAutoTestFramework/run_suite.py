import os
import unittest
import time

from HTMLTestRunner_PY3 import HTMLTestRunner

from apiAutoTestFramework.script.test_tpshop_login import TestTpshopLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTpshopLogin))
report_path = os.path.dirname(os.path.abspath(__file__))+"/report/tpshop{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path,mode='wb')as f:
    runner = HTMLTestRunner(f,verbosity=2,title="TPSHOP登录接口测试",description="HTMLTestRunner_py3生成报告")
    runner.run(suite)