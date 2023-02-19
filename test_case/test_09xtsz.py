
# 产合同管理

import unittest
import jsonpath
from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni

class Xtsz(unittest.TestCase):

    def setUp(self):
        self.sses = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()

    def tearDown(self):
        pass

    # 用户管理
    def test_yhgl(self):
        api_url = "/web/api/res-users"
        url = self.HandleIni.host_url() + api_url
        data = {
            "login": "17620315369@qq.com",      # fake 生成邮箱数据
            "name": "ss",
            "groups_id": [69]
        }

        res = self.sses.login().post(url=url,json=data)
        self.assertEqual(200,res.status_code,True)

        res_json = res.json()
        r_id = jsonpath.jsonpath(res_json,"$..id")
        return r_id


    def test_yhgl_detail(self):
        api_url = "/web/api/ui/views?view=res_users_185&action=res_user&res_ids={}".format(self.test_yhgl())
        url = self.HandleIni.host_url() + api_url
        res = self.sses.login().get(url=url)
        self.assertEqual(200,res.status_code,True)


    # 角色管理


    # 组织架构


    # 消息通知
    def test_xxtz(self):
        api_url = "/web/api/lumi-ui-message"
        url = self.HandleIni.host_url() + api_url
        data = {
            "title": "ffff",
            "type": "system",
            "content": "<slot name=\"content\"></slot><p>hhhjjjj</p>"
        }

        res = self.sses.login().post(url=url,json=data)
        self.assertEqual(200,res.status_code,True)

        res_json = res.json()
        r_id = jsonpath.jsonpath(res_json,"$..id")
        return r_id

    def test_xxtz_detail(self):
        api_url = "/web/api/ui/views?view=lumi_ui_message_181&action=lumi_ui_message_36&res_ids={}".format(self.test_xxtz())
        url = self.HandleIni.host_url() + api_url
        res = self.sses.login().get(url=url)
        self.assertEqual(200,res.status_code,True)



    def test_tijao(self):
        """提交"""
        api_url = "/web/call/message_submit_for_lumi_ui_message"
        url = self.HandleIni.host_url() + api_url
        data = {"context":{},"res_ids":[60],"res_model":"lumi.ui.message","res_id":60,"active_id":60,"active_model":"lumi.ui.message","active_ids":[60]}

        res = self.sses.login().post(url=url,json=data)
        self.assertEqual(200,res.status_code,True)


    def test_shenhe(self):
        """审核"""
        api_url = "/web/call/message_approve_for_lumi_ui_message"
        url = self.HandleIni.host_url() + api_url
        data = {"context": {}, "res_ids": [60], "res_model": "lumi.ui.message", "res_id": 60, "active_id": 60,"active_model": "lumi.ui.message", "active_ids": [60]}

        res = self.sses.login().post(url=url, json=data)
        self.assertEqual(200, res.status_code, True)

    def test_sjujue(self):
        """jujue"""
        api_url = "/web/call/message_reject_for_lumi_ui_message"
        url = self.HandleIni.host_url() + api_url
        data = {"context": {}, "res_ids": [60], "res_model": "lumi.ui.message", "res_id": 60, "active_id": 60,"active_model": "lumi.ui.message", "active_ids": [60]}

        res = self.sses.login().post(url=url, json=data)
        self.assertEqual(200, res.status_code, True)

if __name__=="__main__":
    unittest.main()
