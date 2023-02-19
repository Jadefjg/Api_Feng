import re
import json
import requests

from test_tools.handle_ini import conf
from api.login_session import LoginSession
from test_tools.handle_excel import HandleExcel
from test_tools.handle_attribute import HandleAttribute
from test_tools.handle_sign import HandleSign


class HandleRequest:
    """
      1、发起请求的时候需要鉴权，token放在请求里面，token在类属性
      2、通过封装 requests 实现
        1.查询类属性是否有 token这个 key
        2.如果有就获取这个token，按接口文档去设置请求头里面去，再发起请求
        3.如果没有token，就不处理请求头，直接发起
    """

    def __init__(self):
        self.LoginSesssion = LoginSession()
        #self.HandleExcel = HandleExcel()
        self.headers = {}

    def __handle_headers(self):
        if hasattr(HandleAttribute,'token'):
            self.headers["Authorization"] = "Bearer {}".format(getattr(HandleAttribute,"token"))
        else:
            print("token不存在，无需鉴权")

    # 请求地址的替换
    def __handle_url(self,new_url):
        re_str = r"#(\w.+?)#"
        key_list = re.findall(re_str,new_url)
        if len(key_list) >=1:
            for key in key_list:
                if hasattr(HandleAttribute,key):
                    new_url = new_url.replace(f"#{key}#",str(getattr(HandleAttribute,key)))
                else:
                    print("类属性没有需要替换的数据,用例的参数替换方式写错了,{}".format(key))
            return new_url
        else:
            print("不需要替换请求地址")
            return new_url

    # 请求地址的拼接 + 替换处理
    def __handle_replace_url(self,url):
        base_url = conf.get["host","domain"]
        if url.startswith("http://") or url.startswith("https://"):
            new_url = url
        else:
            new_url = base_url + url
        # 替换请求地址中的数据 member_id
        new_url = self.__handle_url(new_url=new_url)
        return new_url

    # 接口版本的版本鉴权
    def __hanlde_media_type(self,request_data):
        if self.headers[""] == "":
            if hasattr(HandleAttribute,"token"):
                token = getattr(HandleAttribute,"token")
                sign_data = HandleSign.generate_sign(token=token)
                request_data.update(sign_data)
        else:
            print("非V3鉴权方式，不需要处理")
        return request_data

    def send_requests(self,method,url,data):
        try:
            method = method.lower()
            self.__handle_headers()     # token 处理
            # 处理请求地址
            url = self.__handle_replace_url(url=url)
            # 处理版本鉴权
            data = self.__handle_media_type(request_data = data)
            response = requests.request(method=method,url=url,json=data,headers=self.headers)
            # if method == "get":
            #     response = self.LoginSesssion.login.get(url=url,headers=self.headers)
            # else:
            #     response = self.LoginSesssion.login().post(url=url,json=data,headers=self.headers)
            return response.json()
        except Exception as e:
            print("报错信息:{}".format(e))
            raise

