#  登录

import unittest
from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni


class ZZDS_login(unittest.TestCase):

    def setUp(self):
        self.sess = LoginSess()
        self.log = Log
        self.HandleIni = HandleIni()

    def test_login(self):

        #url = ''

        api_url = '/web/login'
        url = self.HandleIni.host_url() + api_url
        data = {
            'login': '',
            'password': '',
        }

        resp = self.sess.login().post(url=url, json=data)
        r_status_code = resp.status_code

        #self.log.info("状态码：%s" % r_status_code)
        self.assertEqual(200,r_status_code,True)

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()


