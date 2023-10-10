import os
import shutil

from test_tools.handle_log import Log
from test_tools.handle_path import report_dir,history_report_dir


class HandleReportsFile:

    @classmethod
    def move_reports_file(cls):
        try:

            # 获取目录下所有文件 或者 目录的mingc
            file_name_list = os.listdir(report_dir)                 # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
            print(file_name_list)
            for file in file_name_list:
                if file.endswith(".html"):                          # endwith() 以“.html”结尾的
                    src = os.path.join(report_dir,file)
                    shutil.move(src=src,dst=history_report_dir)     # src 源文件，递归目录
        except Exception as e:
            Log.error(msg=f'move_reports_file执行报错:{e}')
            Log.exception(e)
            raise Exception("move_reports_file执行报错")



