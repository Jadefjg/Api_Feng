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

    def __replace_data(self, data, key_list):
        """
        使用字符串replace方法替换参数
        :param request_data:
               type=str
               接口请求参数
        :param key_list:
               type=list
               需要替换的参数列表
        :return:
               type=list
               返回替换后的参数
                [mobile_phone,]
        """
        try:
            # 传进来的请求参数必须是str类型
            if isinstance(data, str):
                data = data
            else:
                # 将请求参数强制转换成str类型
                data = str(data)
            for key in key_list:  # for循环进行参数替换
                # 字符串参数替换，必须是字符串类型，这里要转换成字符串
                data = data.replace(f'#{key}#', str(getattr(HandleAttribute, key)))
            return data
        except Exception as e:
            Log.exception(msg=f"__replace_data字符串参数替换报错\n{e}")
            raise Exception("__replace_data字符串参数替换报错")

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

    def __handle_decimal(self, sql_value):
        if isinstance(sql_value, dict):
            sql_value = sql_value
        else:
            sql_value = ast.literal_eval(sql_value)
        if len(list(sql_value.values())) >= 1:
            for key, val in sql_value.items():
                if isinstance(val, Decimal):
                    Log.info(msg=f"将Decimal类型转换成float类型,数据为：{val}")
                    # Decimal(十进制)转换成float类型
                    sql_value[key] = float(val)
                else:
                    pass
                    Log.info(msg="非Decimal类型无需转换成float类型")
            Log.info(msg="将Decimal类型转换成float类型完成")
            return sql_value
        else:
            Log.info(msg="数据库查询出来数据为空，无需将Decimal类型转换成float类型")
        return sql_value

    def replace_check_db_data(self, check_db):
        """
        1、db：先替换sql参数，再查询数据库结果再替换
        2、none：不需要做参数替换，直接拿最后一个值进行替换
        3、其他参数：这里放key，直接去类属性去找，并替换
        :param check_db:
               type=str,dict
               未替换的check_db数据
        :return:
               type=dict
               替换参数后的check_db数据
        """
        try:
            if isinstance(check_db, dict):
                check_db = check_db
            else:
                check_db = ast.literal_eval(check_db)
            # 遍历check_db中期望结果，实际结果key
            for key in check_db.keys():
                tag = check_db[key][0]  # 通过标记为判断替换参数来源
                if tag.upper() == "DB" and len(check_db[key]) >= 2:
                    # 获取替换后的sql
                    replace_sql = self.replace_sql_data(check_db=check_db[key][1])
                    # 执行替换后的sql并获取执行结果
                    sql_value = postgresql.get_db_all_data(sql=replace_sql)
                    new_sql_value = self.__handle_decimal(sql_value=sql_value[0])  # decimal转换成float类型
                    check_db[key] = new_sql_value
                elif tag.upper() == "NONE" and len(check_db[key]) >= 2:
                    # 无需替换，直接取标记后面的值
                    check_db[key] = check_db[key][1]
                else:
                    # key为其他值，从类属性去找，找不到说明标签打错了
                    check_db[key] = getattr(HandleAttribute, check_db[key][0], 'check_db,sql标签有误')
            return check_db
        except Exception as e:
            Log.error(msg=f'check_db参数替换报错:{e}')
            Log.exception(e)
            raise Exception("replace_check_db_data执行报错")

    def replace_request_data(self, request_data, replace_request_data):
        """
        请求参数替换
        1、excel新增请求参数替换规则字段：replace_request_data
        2、创建类属性存储全局变量
        3、通过规则匹配请求字段替换来源
              {"mobile_phone":["conf"]} 从配置文件替换
              {"mobile_phone":["script"]} 从脚本替换
              {"mobile_phone":["db","you_sql"]} #从sql查询结果替换
              {"mobile_phone":["attribute"]} # 全局变量类属性中替换
        4、当前文件新增三个方法
           __get_phone_by_script：从脚本获取(仅手机号)
           __get_data_by_config：从配置文件读取，#name#，name和配置文件的section，option，三者保持一致
           __get_data_by_db：从数据库获取(执行sql脚本)
        5、获取替换规则字段replace_request_data的key作为属性的名称，将需要替换值作为value设置为类属性
        6、通过字符串replace方法循环替换请求参数(字符串替换类型必须是str)
        7、返回替换后的参数dict类型
        :param request_data:
                type=str
                接口请求参数
                {"mobile_phone":"#mobile_phone#","pwd":"Aa123456","type":0,"reg_name":"注册注册注册注册注册"}
        :param replace_request_data:
              type=str
              请求参数替换规则
              {"mobile_phone":["conf"]} 从配置文件替换
              {"mobile_phone":["script"]} 从脚本替换
              {"mobile_phone":["db","you_sql"]} #从sql查询结果替换
              {"mobile_phone":["attribute"]} #全局变量类属性中替换
        :return:
               type = dict
               替换后的参数
               {"mobile_phone":"18820992515"}
        """
        try:
            Log.info(msg="参数替换传入请求参数：\n{},类型为:{}".format(request_data, type(request_data)))
            Log.info(msg="参数替换传入请求参数替换规则：\n{},类型为:{}".format(replace_request_data, type(replace_request_data)))
            if replace_request_data and request_data:
                replace_request_data = ast.literal_eval(replace_request_data)  # 将请求规则参数转成dict格式
                replace_key_list = [key for key in replace_request_data.keys()]  # 获取需要替换的参数的key
                for key, val in replace_request_data.items():
                    if val[0].lower() == "conf":
                        # 从配置文件读取参数，并设置为类属性
                        self.__get_data_by_config(key=key)
                    elif val[0].lower() == "script":
                        if key == "mobile_phone":
                            Log.info(msg="从脚本获取未注册的手机号，并设置为类属性")
                            # 从脚本生成手机号，并设置为类属性，脚本替换参数只支持手机号替换
                            self.__get_phone_by_script(key=key)
                        else:
                            Log.info(msg="从脚本获取仅支持获取未注册的手机号，该字段不支持：{}".format(key))
                    elif val[0].lower() == "db":
                        if len(val) == 2:
                            # 从数据库查询参数，并设置成类属性
                            Log.info(msg="从数据库获取替换参数，并设置为类属性")
                            self.__get_data_by_db(key=key, sql=val[1])
                        else:
                            Log.info(msg="从数据库获取替换参数，没写sql无法替换参")
                    elif val[0].lower() == "attribute":
                        # 从类属性获取参数进行替换
                        Log.info(msg="类属性已存在，从类属性中获取")
                    else:
                        Log.info(msg="该替换参数方式暂不支持:{}".format(val[0]))
                # 参数替换
                new_request_data_by_str = self.__replace_data(data=request_data, key_list=replace_key_list)
                Log.info(msg="请求参数替换完成：\n{},类型为:{}".format(new_request_data_by_str,
                                                                 type(ast.literal_eval(new_request_data_by_str))))
                return ast.literal_eval(new_request_data_by_str)
            elif request_data and not replace_request_data:
                # 有请求参数，但是replace_request_data 参数替换规则为空，说明不需要替换请求参数
                return ast.literal_eval(request_data)
            else:
                # 无请求参数，无替换规则，返回空字典
                return {}
        except Exception as e:
            Log.error('参数替换报错')
            Log.exception(e)
            raise Exception("replace_request_data请求参数替换执行报错")


