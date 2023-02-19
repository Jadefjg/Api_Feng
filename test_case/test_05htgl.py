# 合同管理
import json
import unittest
import jsonpath

from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni

class Htgl(unittest.TestCase):

    def setUp(self,*args,**kwargs):
        self.sess = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()

    # 应用模板配置
    def test_create_template_application(self):
        api_url = "/web/api/setting-template-application"
        url = self.HandleIni.host_url() + api_url

        data = {
            'name': 'test类型01',
            'state': 'disable',
            'description': '哈哈哈哈哈',
            'field_ids': [{
                'code': 'phone_code',
                'name': 'phone',
                'type': 'phone',
                'ir_field_id': 3217
            }]
        }

        resp = self.sess.login().post(url=url, json=data)
        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")
        resp_status_code = resp.status_code
        self.assertEqual(400,resp_status_code,True)
        return r_id


    def test_query_mbpz(self):
        api_url = "/web/api/ui/views?view=setting_template_application_90&action=setting_template_application_28&res_ids={}".format(self.test_create_template_application())
        url = self.HandleIni.host_url() + api_url
        resp = self.Zzds.login().get(url)
        resp_status = resp.status_code
        self.assertEqual(200,resp_status)

    # 状态：禁用 - 启用：http://zzds.pythontest.aqara.com/web/call/setting_template_application_enable_for_setting_template_application

    # 状态：启用 - 禁用：http://zzds.pythontest.aqara.com/web/call/setting_template_application_disable_for_setting_template_application


    # 合同模板配置
    def test_creat_contract_template(self):
        api_url = "/onchange/api/setting-contract-template"
        url = self.HandleIni.host_url() + api_url
        data = {
            "id": "",
            "onchange": "application_ids",
            "values": {
                "name": "合同模板01",
                "a_category": "company",
                "b_category": "personal",
                "attachment": "[{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"20135613203878150311650504215342\",\"size\":2908.71,\"name\":\"打印机指引.pdf\",\"type\":\"application/pdf\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951642474973183.pdf\",\"key\":\"/ZZDS/打印机指引1642474973183.pdf\",\"rename\":\"打印机指引1642474973183.pdf\",\"extName\":\"pdf\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951642474973183.pdf\",\"createTime\":\"2022-01-18 11:02:59\"}]",
                "storage": "",
                "application_ids": [222],
                "template_ids": []
            },
            "fields": {
                "name": "",
                "a_category": "",
                "b_category": "",
                "attachment": "",
                "storage": "",
                "application_ids": "1",
                "template_ids": "",
                "template_ids.application_id": "",
                "template_ids.name": "",
                "template_ids.type": "",
                "template_ids.required": "",
                "template_ids.relation": "",
                "template_ids.setting_id": "",
                "template_ids.field_id": "1"
            }
        }

        resp = self.Zzds.login().post(url=url,json=data)
        resp_status = resp.status_code
        self.assertEqual(200,resp_status)


    def test_creat_contract_template01(self):
        api_url = "/web/api/setting-contract-template"
        url = self.HandleIni.host_url() + api_url
        data = {
            "name":"test合同01",
            "a_category":"personal",
            "b_category":"personal",
            "attachment":"[{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"14713312054055167364821866588737\",\"size\":2908.71,\"name\":\"打印机指引.pdf\",\"type\":\"application/pdf\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951642476841537.pdf\",\"key\":\"/ZZDS/打印机指引1642476841537.pdf\",\"rename\":\"打印机指引1642476841537.pdf\",\"extName\":\"pdf\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951642476841537.pdf\",\"createTime\":\"2022-01-18 11:34:08\"}]",
            "storage":"",
            "application_ids":[
                286
            ],
            "template_ids":[
                {
                    "application_id":{
                        "id":286,
                        "display_name":"test类型03"
                    },
                    "name":"text01",
                    "type":"char",
                    "required":"yes",
                    "relation":"a",
                    "field_id":{
                        "id":488,
                        "display_name":"text01"
                    }
                }
            ]
        }
        resp = self.Zzds.login().post(url=url,json=data)
        resp_status = resp.status_code
        self.assertEqual(200,resp_status,True)

    def test_save_for__setting_conttract_template(self):
        api_url = "/web/call/save_for_setting_contract_template"
        url = self.HandleIni.host_url() + api_url
        data = {
            "context":{

            },
            "res_ids":[
                116
            ],
            "res_model":"setting.contract.template",
            "res_id":116,
            "active_id":"",
            "active_model":"setting.contract.template",
            "active_ids":[

            ],
            "view_data":{
                "name":"test合同01",
                "a_category":"personal",
                "b_category":"personal",
                "attachment":"[{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"14713312054055167364821866588737\",\"size\":2908.71,\"name\":\"打印机指引.pdf\",\"type\":\"application/pdf\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951642476841537.pdf\",\"key\":\"/ZZDS/打印机指引1642476841537.pdf\",\"rename\":\"打印机指引1642476841537.pdf\",\"extName\":\"pdf\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951642476841537.pdf\",\"createTime\":\"2022-01-18 11:34:08\"}]",
                "storage":"",
                "application_ids":[
                    286
                ],
                "template_ids":[
                    {
                        "application_id":{
                            "id":286,
                            "display_name":"test类型03"
                        },
                        "name":"text01",
                        "type":"char",
                        "required":"yes",
                        "relation":"a",
                        "field_id":{
                            "id":488,
                            "display_name":"text01"
                        }
                    }
                ]
            }
        }

        resp = self.Zzds.login().post(url=url,json=data)
        resp_status = resp.status_code
        self.assertEqual(200,resp_status,True)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



