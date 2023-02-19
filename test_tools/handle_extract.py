
import ast
from jsonpath import jsonpath
from test_tools.handle_attribute import HandleAttribute


class HandleExtract:

    def __set_attibute(self,key,val):
        setattr(HandleAttribute,key,val)

    def handle_extract(self,response,extract_data):

        # 1、判断提取的数据是否为空，不为空才提取数据
        if extract_data:
            # 2、对数据类型进行处理，转换成 python 对象，dict
            if isinstance(extract_data,dict):
                extract_data = extract_data
            else:
                extract_data = ast.literal_eval(extract_data)
            # 3、通过提取表达式获取提取的数据，再设置成类属性
            for key,value in extract_data.items():
                extract_result = jsonpath(response,value)
                self.__set_attibute(key=key,val=extract_result[0])
        else:
            print("extract_data无需从response中提取参数")


