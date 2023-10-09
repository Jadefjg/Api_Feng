""" 数据库校验 """

import ast
from unittest import TestCase
from test_tools.handle_replace import HandleReplace
from test_tools.handle_db import postgresql


class HandleCheckDb:

    def __init__(self):
        self.replace = HandleReplace()

    # 数据库断言
    def check_db(self,check_db,replace_data):
        if check_db:
            # 执行表达式，转换为 python 对象(dict)
            check_db = ast.literal_eval(check_db)
            # 期望结果
            expect_data = check_db["expect_data"]
            # 实际结果
            actual_data = check_db["actual_data"]
            # 替换sql语句
            new_sql = self.replace.replace_sql_data(sql=actual_data,replace_data=replace_data)
            # 执行 sql 语句，获取执行结果
            new_sql_result = postgresql.get_db_all_value_list(sql=new_sql)
            # 断言(实际结果与期望结果进行比对)
            TestCase().assertEqual(expect_data,new_sql_result[0])
        else:
            print("不需要对数据库做断言")




