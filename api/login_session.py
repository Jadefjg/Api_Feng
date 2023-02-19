# 目标：获取登录会话

import re
import requests
from pprint import pprint

class LoginSession:
    def __init__(self):
        self.s = requests.session()

    def login(self):

        RE_CSRF = re.compile(r'csrf_token" value="(?P<csrf_token>[a-z\d]+)"')

        login_url = "http://ac-sit.pythontest.aqara.com/web/login?redirect=http://ac-sit.pythontest.aqara.com/sso/login?system_name=xls&system_url=http:%2F%2Fzzds.pythontest.aqara.com%2F%23%2F&redirect=http:%2F%2Fzzds.pythontest.aqara.com%2F%23%2F"
        redirect_url = 'http://ac-sit.pythontest.aqara.com/sso/login?system_name=xls&system_url=http:%2F%2Fzzds.pythontest.aqara.com%2F%23%2F&redirect=http:%2F%2Fzzds.pythontest.aqara.com%2F%23%2F'

        # 登录地址
        resp = self.s.get(login_url)
        html = resp.text
        csrf = RE_CSRF.search(html).group('csrf_token')
        pprint(csrf)

        data = {
            'csrf_token': csrf,
            'login': 'jiagang.feng-a1777@aqara.com',
            'password': 'Feng666666',
            'redirect': redirect_url
        }

        # 登陆提交
        resp = self.s.post('http://ac-sit.pythontest.aqara.com/web/login', data=data)
        # pprint(resp)
        last_url = resp.request.url
        print(last_url)
        params = last_url.split('?')[-1]
        url = f'http://zzds.pythontest.aqara.com/web/ui_login?{params}'
        resp = self.s.get(url)
        print(resp)
        return self.s

# A = LoginSession()
# res = A.login().get("http://zzds.pythontest.aqara.com/web/api/ui/menus")
# print(res.status_code)