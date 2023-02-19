import unittest
import unittestreport
from test_tools.handle_path import case_dir,report_dir,report_name
from test_tools.handle_reports_file import HandleReportsFile

# 先将 reports 目录下的.html测试报告挪走
HandleReportsFile.move_reports_file()

# 测试套件
suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test_all.py")

runner = unittestreport.TestRunner(
    suite = suite,
    filename=report_name,
    report_dir=report_dir,
    title="接口测试报告",
    tester='feng',
    desc="Api_Feng",
    templates=2
)

runner.run()


# 调试代码期间注释该代码，以免频繁的发邮件给用户造成困扰。发布时候要取消注释
# runner.send_email(host="smtp.163.com",
#                   port=465,
#                   user="fjgjiagang@163.com",
#                   password="UGMMRZNAEAMCTFMG",
#                   to_addrs="2513635177@qq.com"
#                   )

