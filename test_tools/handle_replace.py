""" 数据替换 """

import re
import ast
from decimal import Decimal

from test_tools.handle_ini import conf
from conf.settings import replace_data
from test_tools.handle_db import postgresql
from test_tools.handle_phone import HandlePhone     # 获取未注册的手机号码
from test_tools.handle_attribute import HandleAttribute
from test_tools.handle_log import Log


class HandleReplace:

    def __init__(self):
        self.handle_phone = HandlePhone()

    def __get_phone_by_script(self, key):
        # 脚本生成未注册过的手机号，并设置为类属性
        phone = self.handle_phone.get_phone()
        self.__set_attribute(key=key, val=phone)

    def __get_data_by_config(self, key):
        # 从配置文件读取数据，并设置为类属性
        data = conf.get(section=key, option=key)
        self.__set_attribute(key=key, val=data)

    def __get_data_by_db(self, key, sql):
        """
            数据库查询数据，将查询结果设置为类属性
            :param key:
                   type=str
                   类属性的key名称
            :param sql:
                   type=str
                   sql语句，只支持一条数据
                       select mobile_phone from member where mobile_phone=18820992515
            :return:无返回,这里还要看一下是否兼容多个
        """
        data = postgresql.get_db_all_data(sql)
        # 这里数据库查询返回的是字典{id:123456}，这里要取字典的value
        for val in data[0].values():
            self.__set_attribute(key=key, val=val)

    # 设置类属性
    def __set_attribute(self,key,val):
        setattr(HandleAttribute,key,val)

    # 获取数据库数据设置为类属性
    def __execute_sql_and_settattr(self,sql):
        """执行sql语句，并将sql获取到的数据设置为类属性"""
        result = postgresql.get_db_all_data(sql=sql)
        for dict_data in result:
            for key,val in dict_data.items():
                self.__set_attribute(key=key,val=val)

    # 将需要替换的参数(原始数据)，从对应的渠道(配置文件)获取到对应的结果，设置为类属性
    def __set_attribute_data(self,key_list,replace_data,sql=None):
        """
            :param key_list：拿到需要替换数据的名称，list=["phone"]
            :param replace_data
            :param sql:replace_sql
            :return:
            1、设置类属性
            2、从脚本获取手机号，设置为类属性
            3、从数据库获取数据，设置为类属性

            需求要替换的数据 key_list, list=["phone"]
            配置文件(ini、yaml、py、excel、sql)获取替换的数据(新数据)
        """

        if sql:
            for i in ast.literal_eval(sql):
                self.__execute_sql_and_settattr(sql=i)

        for key in key_list:
            if key == "phone":
                phone = self.handle_phone.get_phone()
                self.__set_attribute(key=key,val=phone)
            elif key in replace_data:
                self.__set_attribute(key=key,val=replace_data[key])
            else:
                pass

    # 获取替换的数据(原数据)
    def __get_replace_keys(self,data):
        re_str = r"#(\#.+?)#"
        key_list = re.findall(re_str,str(data))
        return key_list

    # 参数替换
    def replace_data(self,data,sql=None):
        if data:
            key_list = self.__get_replace_keys(data=data)
            if len(key_list)>0:
                # 1、根据数据来源区获取 + 2、设置类属性
                self.__set_attribute_data(key_list=key_list,replace_data=replace_data,sql=sql)
                # 3、进行参数替换
                for key in key_list:
                    data = data.replace("#{}#".format(key).str(getattr(HandleAttribute,key)))
                return ast.literal_eval(data)
            else:
                return ast.literal_eval(data)
        else:
            return {}

    # 替换 sql 参数
    def replace_sql_data(self,sql,replace_data):
        if sql:
            key_list = self.__get_replace_keys(data=sql)
            if len(key_list)>0:
                for key in key_list:
                    if key == "phone":
                        print("phone已经存在类属性中，无需重新设置")
                    elif key in replace_data:
                        self.__set_attribute(key=key,val=replace_data[key])
                    else:
                        print("暂时不支持你的参数设置渠道，自己拓展")

                for key in key_list:
                    sql = sql.replace("#{}#".format(key),str(getattr(HandleAttribute,key)))
            return sql
        else:
            print("sql数据为空，不需要替换sql语句")


