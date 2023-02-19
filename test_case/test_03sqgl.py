# 商圈现状：查询，门店数(数据库与接口返回的数据对比)
import unittest
import jsonpath

from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni

class sqgl_zzkh(unittest.TestCase):

    def setUp(self, *args, **kw):
        self.sess = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()

    def tearDown(self):
        pass

    def test_query_company(self):
        api_url = '/web/api/shang-exam/query?offset=0&limit=10&fields=[%22shang_name_id%22,%22affiliate_stage%22,%22shop_level%22,%22city_level_id%22,%22achievement%22,%22test_achievement%22,%22remainder_day%22,%22manager_ids%22]&order=id%20desc&domains=[]'
        url = self.HandleIni.host_url()+api_url
        resp = self.sess.login().get(url=url)
        r_id = jsonpath.jsonpath(resp, "$..id")
        self.log.info("招商的ID：%s" % r_id)
        #self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code,msg="查询公司")
        return r_id

    def test_query_zs(self):
        api_url = '/web/api/ui/views?view=shang-management-information-form&action=shang-management-information&res_ids={}'.format(self.test_query_company())
        url = self.HandleIni.host_url()+api_url
        resp = self.Zzds.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code,msg="查询接口")

if __name__=="__main__":
    unittest.main()










