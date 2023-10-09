""" 数据库校验 """

import ast
from unittest import TestCase
from test_tools.handle_replace import HandleReplace
from test_tools.handle_db import postgresql
from test_tools.handle_log import Log


class HandleCheckDb:

    def __init__(self):
        self.handle_replace = HandleReplace()

    # 获取查询结果，并返回结果。 单条 sql 的查询结果
    def __get_db_result(self,sql):
        Log.info(msg="数据库字段校验查询sql：\n{}".format(sql))
        result = postgresql.get_db_all_data(sql=sql)
        Log.info(msg="数据库查询返回：\n{}".format(result))

    def setup_sql(self,sql_List):
        """
            :param sql_list:
                   :type=list
                   sql语句
            :return: 无
        """
        try:
            if sql_List:
                if isinstance(sql_List,list):   # isinstance(sql_list,list): 判断 sql_list 的数据类型为 List
                    sql_List = sql_List
                else:
                    sql_List = ast.literal_eval(sql_List)    # literal_eval()函数：则会判断需要计算的内容计算后是不是合法的python类型，如果是则进行运算，否则就不进行运算。
                Log.info(msg="执行初始化sql语句，只执行，不设置全局变量")
                for sql in sql_List:
                    postgresql.get_db_all_data(sql=sql)     # 执行 sql 获取所有的数据。多条 sql 语句的查询结果
            else:
                Log.info(msg="初始化sql字段为空，不需要执行初始化sql")
        except Exception as e:
            Log.exception(e)
            raise Exception("前置sql执行报错")

    def check_db(self,check_db):
        """
              check_db：
              :param check_db:
                     type=str
                     传入excel中check_db整个字段参数
              :param expected_data:
                     type=dict
                     期望结果
              :param actual_data:
                     type=dict
                     实际结果
              :return: 无返回
        """
        if check_db:
            # 获取替换后的 check_db数据
            check_db = self.handle_replace.replace_sql_data(check_db=check_db)
            check_db = ast.literal_eval(check_db)
            # 获取实际结果sql语句
            actual_data_sql = check_db['actual_data']
            # 执行实际结果sql，获取执行结果
            db_result = self.__get_db_result(sql=actual_data_sql)
            # 数据库获取的结果替换预期结果
            check_db['actual_data'] = str(len(db_result))
            Log.info(msg='数据库校验期望结果:\n{}'.format(check_db['expected_data']))
            Log.info(msg='数据库校验实际结果:\n{}'.format(check_db['actual_data']))
            Log.info(msg="sql校验替换后的参数:{}".format(check_db))

            if check_db['expected_data'] == check_db['actual_data']:
                Log.info(msg='数据库断言成功')
            else:
                Log.info(msg='数据库断言失败')
                raise AssertionError
        else:
            Log.info(msg='无需做数据校验')

    # 检查新数据
    def check_db_new(self, check_db):
        """
            一、sql替换场景
                1、不需要
                2、通过sql查询数据库
                3、全局变量属性里面有，直接替换
            二、check_db字段格式：
                check_db={
                "actual_data":["db","select mobile_phone from member where mobile_phone = '#mobile_phone#'"],
                "expected_data":["none","18820992515"]
                "expected_data":["mobile_phone"]
                }
            1、db：先替换db参数，再查询数据库结果再替换
            2、none：不需要做参数替换，直接拿最后一个值进行替换
            3、其他参数：这里放key，直接去类属性去找，并替换
            :param check_db:
                   type=str,dict
                   传入excel中check_db整个字段参数
            :param expected_data:
                   type=dict
                   期望结果
            :param actual_data:
                   type=dict
                   实际结果
            :return:无返回
        """
        try:
            if check_db:
                if isinstance(check_db, dict):
                    check_db = check_db
                else:
                    check_db = ast.literal_eval(check_db)
                # check_db参数替换之后，{'actual_data': {'count': 1}, 'expected_data': {'count': 1}}
                new_check_db = self.handle_replace.replace_check_db_data(check_db=check_db)
                Log.info(msg='数据库校验期望结果:\n{}'.format(new_check_db['expected_data']))
                Log.info(msg='数据库校验实际结果:\n{}'.format(new_check_db['actual_data']))
                # 取字符串第一位判断是否是数字，不能拿整个去判断，isdigit()不认识小数点
                assert new_check_db['expected_data'] == new_check_db['actual_data']
            else:
                Log.info(msg='无需做数据校验')
        except Exception as e:
            Log.error(msg='check_db数据库参数校验报错')
            Log.exception(e)
            raise AssertionError

    def check_db_many_start_request(self, check_db_many):
        """
            请求前后数据库校验，请求发起前替换sql参数，并获取sql执行结果
                1、先替换sql中需要替换的参数
                2、再执行sql拿到结果
                3、替换first、second的值
            :param check_db_many:
                   type=str,dict
                   excel中check_db_many字段的值
                   {
                   "first":["db","your_sql"],
                   "second":["db","your_sql"],
                   "last":["db","your_sql"],
                   "update_db":["update_db","your_sql"],
                   "expected_data":["first","second","+"],
                   "actual_data":["sql","your_sql"]
                   }
            :return:
                   type=str
                   替换掉sql参数后的值
        """
        try:
            if check_db_many:
                if isinstance(check_db_many, dict):
                    check_db_many = check_db_many
                else:
                    check_db_many = ast.literal_eval(check_db_many)
                # 期望结果(expected_data),实际结果(actual_data)
                # 其他的都是接口请求之前需要替换的sql，拿到替换后的结果再与原始的dict合并，等请求完接口之后再进行替换和数据校验
                replace_dict = {}
                for key in check_db_many.keys():
                    if key != "expected_data" and key != "actual_data":
                        # replace_dict 为字典，收集需要替换的sql的键值对
                        replace_dict[key] = check_db_many[key]
                    else:
                        pass
                # 替换replace_dict中key的val,这里的val{'first': Decimal('1100301.00')}类型要转换成float
                # 新增
                new_check_db_many = self.handle_replace.replace_check_db_data(check_db=replace_dict)
                # 更新后的数据与原来数据进行合并，此时更新后就是可以执行的sql语句，{"member_phone":"select * from member where mobile_phone=18820992515"}
                check_db_many.update(new_check_db_many)
                return check_db_many
            else:
                return check_db_many
        except Exception as e:
            Log.error('接口执行前,需要替换sql并保留数据，执行失败')
            Log.exception(e)
            raise AssertionError

    def __handle_check_db_many_expected_data(self, check_db_many, expected_data):
        """
            check_db_many_end_request方法中期望结果处理
            :param check_db_many:
                    :type=dict
                    excel中check_db_many字段的值
            :param expected_data:
                   :type=dict
                   excel中期望期望结果
            :return:
                   :type=dict
                   expected_data
                   按规则计算后的期望结果
        """
        try:
            # 获取期望结果计算规则,expected_rule="first+second+last""
            expected_rule = expected_data["expected_data"]
            for key in check_db_many.keys():
                if key in expected_rule:
                    one_vaule = list(check_db_many[key].values())[0]
                    expected_rule = expected_rule.replace(key, str(one_vaule))
            # 期望结果计算后的值
            expected_data_value = eval(expected_rule)
            Log.info(msg="期望结果按照规则计算后的值:{}".format(expected_data_value))
            # 用计算后的期望结果，更新期望结果
            expected_data["expected_data"] = expected_data_value
            return expected_data
        except Exception as e:
            Log.exception(e)
            raise AssertionError

    def check_db_many_end_request(self, check_db_many):
        """
            请求前后数据库校验，请求发起前替换sql参数，并获取sql执行结果
            :param check_db_many:
                   type=str,dict
                   excel中check_db_many字段的值
                   {
                   "first":100,
                   "second":200,
                   "last":300,
                   "expected_data":"first+1000"],
                   "actual_data":["db","your_sql"]
                   }
                   1、actual_data 中sql替换掉，再替换掉["sql","your_sql"]，为sql 执行结果
                   2、将规则["first","second","+"]中的标记位，替换成实际的值(执行接口之前查询到的值)
                   3、"expected_data":["100","200","+"], 替换成计算后的结果
                   4、断言actual_data，expected_data
            :return:无
                   直接在这里比对断言
        """
        try:
            if check_db_many:
                if isinstance(check_db_many, dict):
                    check_db_many = check_db_many
                else:
                    check_db_many = ast.literal_eval(check_db_many)
                    # 替换replace_dict中key的val
                Log.info(msg='传入的参数：{}'.format(check_db_many))

                # 创建实际结果对象,替换实际结果，获取替换后的实际结果
                actual_data = {"actual_data": check_db_many["actual_data"]}
                Log.info(msg="实际结果替换之前\n{}".format(actual_data))
                # 获取替换后的实际结果，新增
                new_actual_data = self.handle_replace.replace_check_db_data(check_db=actual_data)
                # 获取实际结果具体数据
                new_actual_data = list(new_actual_data["actual_data"].values())[0]
                Log.info(msg="实际结果替换后\n{}".format(new_actual_data))

                # 创建预期结果对象
                expected_data = {"expected_data": check_db_many["expected_data"]}
                Log.info(msg="预期结果替换之前\n{}".format(expected_data))

                # 获取按规则计算并替换后的期望结果，可以直接比较
                new_expected_data = self.__handle_check_db_many_expected_data(check_db_many=check_db_many,
                                                                              expected_data=expected_data)
                Log.info(msg="预期结果替换后\n{}".format(expected_data))

                # 期望结果expected_data，实际结果actual_data 断言,数字通过float对比，其他的通过str对比
                assert new_expected_data["expected_data"] == new_actual_data
            else:
                Log.info(msg="多重数据库校验，check_db_many为空不需要校验")
        except Exception as e:
            Log.error("多重数据库校验，执行出错")
            Log.exception(e)
            raise AssertionError





    # # 数据库断言
    # def check_db(self,check_db,replace_data):
    #     if check_db:
    #         # 执行表达式，转换为 python 对象(dict)
    #         check_db = ast.literal_eval(check_db)
    #         # 期望结果
    #         expect_data = check_db["expect_data"]
    #         # 实际结果
    #         actual_data = check_db["actual_data"]
    #         # 替换sql语句
    #         new_sql = self.handle_replace.replace_sql_data(sql=actual_data,replace_data=replace_data)
    #         # 执行 sql 语句，获取执行结果
    #         new_sql_result = postgresql.get_db_all_value_list(sql=new_sql)
    #         # 断言(实际结果与期望结果进行比对)
    #         TestCase().assertEqual(expect_data,new_sql_result[0])
    #     else:
    #         print("不需要对数据库做断言")




