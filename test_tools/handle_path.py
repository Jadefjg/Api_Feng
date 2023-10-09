import os
import time


# 基础路径：D:\workspace\PycharmProjects\Api_Feng
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据
case_data_dir = os.path.join(base_dir,"test_data","testCase.xlsx")

# 测试文件夹
case_dir = os.path.join(base_dir,'test_case')

# 配置文件路径
conf_dir = os.path.join(base_dir,"conf","cfg.ini")

# 日志文件路径
log_file_name = time.strftime("%Y%m%d",time.localtime())
log_dir = os.path.join(base_dir,'logs','{}.log'.format(log_file_name))

# 报告文件路径
report_dir = os.path.join(base_dir,'reports')
report_name = time.strftime("%Y%m%d_%H%M%S.html",time.localtime())
history_report_dir = os.path.join(base_dir,'reports','history') # 历史报告文件路径