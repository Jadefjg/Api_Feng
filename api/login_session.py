# 目标：获取登录会话

import re
import requests
from pprint import pprint


class LoginSess:
    def __init__(self):
        self.s = requests.session()

    def login(self):

        RE_CSRF = re.compile(r'csrf_token" value="(?P<csrf_token>[a-z\d]+)"')

        login_url = ""
        redirect_url = ''

        # 登录地址
        resp = self.s.get(login_url)
        html = resp.text
        csrf = RE_CSRF.search(html).group('csrf_token')
        pprint(csrf)

        data = {
            'csrf_token': csrf,
            'login': '',
            'password': 'Feng666666',
            'redirect': redirect_url
        }

        # 登陆提交
        resp = self.s.post('', data=data)
        # pprint(resp)
        last_url = resp.request.url
        print(last_url)
        params = last_url.split('?')[-1]
        url = f'?{params}'
        resp = self.s.get(url)
        print(resp)
        return self.s

# A = LoginSession()
# res = A.login().get("")
# print(res.status_code)