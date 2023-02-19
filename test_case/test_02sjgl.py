# 商家信息

import unittest
import jsonpath

from api.login_session import LoginSession
from test_tools.handle_log import Log
from conf.readConf import HandleIni


# 商家管理 - 商家信息
class sjgl_sjxx(unittest.TestCase):

    def setUp(self, *args, **kw):
        self.sess = LoginSession()
        self.log = Log()
        self.HandleIni = HandleIni()

    def test_query_company(self):
        api_url = '/web/api/shang-management-information/query?offset=0&limit=10&fields=[%22name%22,%22region_id%22,%22affiliate_category_id%22,%22affiliate_stage%22,%22store_count%22,%22connect_name%22,%22phone%22,%22regist_district_id%22,%22audit_time%22,%22forward_time%22,%22manager_ids%22,%22authentication_state%22,%22state%22,%22regist_province_id%22,%22regist_city_id%22]&order=id%20desc&domains=[]'
        url = self.HandleIni.host_url() + api_url


        resp = self.sess.login().get(url=url)
        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")[0]   # .data.value.id
        self.log.info("招商的ID：%s" % r_id)
        #self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code,True)
        return r_id

    def test_query_zs(self):
        api_url = '/web/api/ui/views?view=shang-management-information-form&action=shang-management-information&res_ids={}'.format(self.test_query_company())
        url = self.HandleIni.host_url() + api_url
        resp = self.sess.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code,True)


    # 商家管理 - 转正考核
    def test_query_company(self):
        api_url = '/web/api/shang-exam/query?offset=0&limit=10&fields=[%22shang_name_id%22,%22affiliate_stage%22,%22shop_level%22,%22city_level_id%22,%22achievement%22,%22test_achievement%22,%22remainder_day%22,%22manager_ids%22]&order=id%20desc&domains=[]'
        url = self.HandleIni.host_url() + api_url
        resp = self.sess.login().get(url=url)
        resp_json=resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")[0]
        self.log.info("招商的ID：%s" % r_id)
        #self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code,True)
        return r_id

    def test_query_zs(self):
        api_url = '/web/api/ui/views?view=shang-management-information-form&action=shang-management-information&res_ids={}'.format(self.test_query_company())
        url = self.HandleIni.host_url()+api_url
        resp = self.sess.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code,True)

if __name__=="__main__":
    unittest.main()

