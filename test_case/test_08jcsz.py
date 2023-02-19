# 基础配置

import unittest
import jsonpath
from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni

class jcpz(unittest.TestCase):

    def setUp(self):
        self.sess = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()

    def tearDown(self):
        pass

    # 城市等级配置
    def test_cspz_create(self):
        api_url = "/web/api/setting-city-level"
        url = self.HandleIni.host_url()+api_url
        data = {
            "level_name": "和电话多好多好",
            "exam_day": 5,
            "range": "10",
            "achievement_request": 10000,
            "district_ids": [3784, 3785, 3786, 3787]
        }

        res = self.sess.login().post(url=url,json=data)
        print(res.json())
        self.assertEqual(200,res.status_code,True)

    def test_cspz_xiangqing(self):
        api_url = "/web/api/ui/views?view=setting_city_level_110&action=setting_city_level_24&res_ids={}".format(self.test_cspz_create())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        self.assertEqual(200,res.status_code,True)


    # 招商渠道
    def test_zsqd(self):
        api_url = "/web/api/shang-channel"
        url = self.HandleIni.host_url() + api_url
        data = {"name":"大家的积极","code":"JMLX000000"}
        res = self.sess.login().post(url=url,json=data)
        self.assertEqual(200,res.status_code,True)

        res_json = res.json()
        r_id = jsonpath.jsonpath(res_json,"$..id")
        return r_id

    def test_zsqd_detatial(self):
        api_url = "/web/api/ui/views?view=channel-form&action=channel&res_ids={}".format(self.test_zsqd())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        self.assertEqual(200,res.status_code,True)

    # 加盟类型
    def test_jmlx(self):
        api_url = "/web/api/join-type"
        url = self.HandleIni.host_url() + api_url
        data = {"name": "大家的积极", "code": "JMLX000000"}
        res = self.sess.login().post(url=url, json=data)
        self.assertEqual(200, res.status_code, True)

        res_json = res.json()
        r_id = jsonpath.jsonpath(res_json, "$..id")
        return r_id

    def test_jmlx_detatial(self):
        api_url = "/web/api/ui/views?view=join-type-form&action=join-type&res_ids={}".format(self.test_jmlx())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        self.assertEqual(200, res.status_code, True)

    # 区域配置
    def test_qypz(self):
        api_url = "/web/api/setting-region"
        url = self.HandleIni.host_url() + api_url
        data = {"name": "大家的积极", "code": "JMLX000000"}
        res = self.sess.login().post(url=url, json=data)
        self.assertEqual(200, res.status_code, True)

        res_json = res.json()
        r_id = jsonpath.jsonpath(res_json, "$..id")
        return r_id

    def test_qypz_detatial(self):
        api_url = "/web/api/ui/views?view=setting_region_105&action=setting_region_29&res_ids={}".format(self.test_qypz())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        self.assertEqual(200, res.status_code, True)


if __name__=="__main__":
    unittest.main()
