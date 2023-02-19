"""
    1、执行核心的业务流程
    2、造各种类型的账号，数据
"""

import ast
import unittest
from ddt import ddt,data

from test_tools.handle_log import test_log
from test_tools.handle_db import postgresql
from test_tools.handle_excel import HandleExcel
from test_tools.handle_path import case_data_dir
from test_tools.handle_replace import HandleReplace
from test_tools.handle_request import HandleRequest
from test_tools.handle_extract import HandleExtract
from test_tools.handle_check_db import HandleCheckDb
from conf.settings import excel_sheet,replace_data
#from unittestreport import ddt, list_data

case_list = HandleExcel(file_name=case_data_dir,sheet_name=excel_sheet["all"]).get_test_case()
print(case_list)

@ddt
class TestAll(unittest.TestCase):
    @classmethod     # @classmethod 修饰符号对应的函数不需要实例化，不需要 self 参数，但第一个参数需要表示自身类的 cls 参数，可以来调用类的属性，类方法，实例化对象等
    def setUpClass(cls) -> None:
        cls.hanlde_replace = HandleReplace()
        cls.handle_check_db = HandleCheckDb()
        cls.handle_extract = HandleExtract()
        cls.handle_request = HandleRequest()

    @classmethod
    def tearDownClass(cls) -> None:
        postgresql.close()

    @data(*case_list)
    def test_all(self,case):
        try:
            # 1、性质前置 sql 语句
            if case["setup_sql"]:
                for sql in ast.literal_eval(case["setup_sql"]):
                    # 执行 sql 语句
                    postgresql.get_db_all_data(sql=sql)

            # 2、参数替换
            # 造数据：fake, 正则表达式：re, 数据提取：jsonpath
            new_data = self.hanlde_replace.replace_data(data=case["data"],sql=case["replace_sql"])

            # 3、执行之前，将需要断言的数据保存下来，
            first_result = 0
            if str(case["check_dy_dynamic"]) == "1":
                sql1 = ""
                first_result = postgresql.get_db_all_value_list(sql=sql1)
                first_result = float(first_result[0])
                print("接口请求前数据：",first_result)

            # 4、发送 requests 请求，post,get,patch
            response = self.handle_request.send_requests(method=case["method"],url=case["url"],data=new_data)

            # 5、接口断言
            # 生成最 new_url
            # new_url = host["base_url"] + case["url"]
            # 发送 requests 请求，post、get、patch
            # response = self.hand_request.send_requests(method=case["method"],url=new_url,data=case["request_data"])
            actual_data = {"code":response["code"],"status":response["status"],"message":response["message"]}
            expect_data = case["expect_data"]       # 从 excel 表格提取数据
            self.assertEqual(ast.literal_eval(expect_data),actual_data)

            # 6、从响应数据提取参数
            self.handle_extract.handle_extract(response=response,extract_data=case["extract_data"])

            # 7、数据库断言
            self.handle_check_db.check_db(check_db=case["check_db"],replace_data=replace_data)

            # 8、【获取接口执行后的断言数据】，数据库动态校验
            if str(case["check_db_dynamic"]) == "1":
                sql1 = ""
                second_result = postgresql.get_db_all_value_list(sql=sql1)
                second_result = float(second_result[0])
                self.assertEqual(100,first_result - second_result)
        except Exception as e:
            test_log.exception(e)
            raise AssertionError
