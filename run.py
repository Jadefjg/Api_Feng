import os
import time
import unittest
import HTMLTestRunner

from test_tools.handle_reports_file import HandleReportsFile
from test_tools.handle_path import case_dir,report_dir,report_name

# 先将 reports 目录下的.html测试报告挪走
HandleReportsFile.move_reports_file()

# 测试套件
suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test_all.py",top_level_dir=None)

now = time.strftime("%Y_%m_%d_%H_%M_%S")
report_abspath = os.path.join(report_dir, now + "result.html")
fp = open(report_abspath, "wb")

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u'自动化测试报告,测试结果如下：',
                                       description=u'用例执行情况：')

runner.run(suite)

