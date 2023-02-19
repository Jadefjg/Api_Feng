"""
1、判断手机号是否注册
2、手机号已经注册就提示注册，手机号未注册就显示，并被后续引用。
"""

from faker import Faker
from test_tools.handle_db import postgresql

class HandlePhone:

    def __init__(self):
        self.fk = Faker(locale="zh-cn")

    def __faker_phone(self):
        phone = self.fk.phone_number()
        return phone

    def __select_phone(self,phone):
        # 查询数据库结果
        sql = "select * from shang_join_information where phone = '{}'".format(phone)
        result = postgresql.get_db_all_value_list(sql=sql)
        return result

    def get_phone(self):
        while True:
            phone = self.__faker_phone()    # 生成手机号码
            result = self.__select_phone(phone=phone)   # 查询数据库结果
            if len(result) > 0:   # 判断是否已注册
                # 重新生成
                continue
            else:
                # 返回未注册的手机号
                return phone


test = HandlePhone()
result = test.get_phone()
print(result)




