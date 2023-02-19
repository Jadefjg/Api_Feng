
import unittest
from test_tools.handle_log import Log
from api.login_session import LoginSess
from conf.readConf import HandleIni


class ZZDS_login(unittest.TestCase):

    def setUp(self,*args,**kwargs):
        self.log = Log()
        self.sess = LoginSess()
        self.HandleIni = HandleIni()

    def test_logout(self):
        # url = ""
        # api_url = '/web/ui_logout'
        # url = self.HandleIni.host_url() + api_url

        api_url = '/web/ui_logout'
        url = self.HandleIni.host_url() + api_url

        resp = self.sess.login().get(url=url)
        r_status_code = resp.status_code
        self.log.info("状态码：%s" % r_status_code)

        self.assertEqual(200,r_status_code,True)

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()




