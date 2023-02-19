# 合同管理
import unittest
import jsonpath

from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni

class scgl(unittest.TestCase):

    def setUp(self,*args,**kwargs):
        self.sess = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()
    # 素材信息
    def test_create_sucai(self):
        api_url = '/web/api/material-information'
        url = self.HandleIni.host_url() + api_url
        data = {
            "name":"思思",     # 素材名称校验唯一性
            "classify_id":140,
            "open_range_ids": None,
            "description":"好的好的",
            "state":"draft",
            "material":"[{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"22977938123957520481020412747797\",\"size\":27.93,\"name\":\"mi.jpeg\",\"type\":\"image/jpeg\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/mi1642489250628.jpeg\",\"key\":\"/ZZDS/mi1642489250628.jpeg\",\"rename\":\"mi1642489250628.jpeg\",\"extName\":\"jpeg\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/mi1642489250628.jpeg\",\"createTime\":\"2022-01-18 16:00:50\"}]"
        }

        resp = self.sess.login().post(url=url,json=data)
        resp_status = resp.status_code
        self.assertEqual(200, resp_status, True)

        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "..id")
        print(r_id)
        return r_id

    def test_scxx(self):
        api_url = "/web/api/ui/views?view=material_information_57&action=material_information_16&res_ids={}".format(self.test_create_sucai())
        url = self.HandleIni.host_url() + api_url
        resp = self.sess.login().get(url)
        resp_status = resp.status_code
        self.assertEqual(200,resp_status,True)

    # 素材分类
    def test_scfl(self):
        api_url = "/web/api/material-classify"
        url = self.HandleIni.host_url()+api_url
        data = {
            "name": "素材分类01",
            "description": "哈哈哈扩扩扩扩",
            "state": "draft",
            "active": True
        }
        resp = self.sess.login().post(url=url,json=data)
        resp_status = resp.status_code
        self.assertEqual(200,resp_status,True)

        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json,"..id")
        print(r_id)
        return r_id

    def test_query(self):
        api_url = "/web/api/ui/views?view=material_classify_50&action=material_classify_15&res_ids={}".format(self.test_create_scfl())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url)
        res_status = res.status_code
        self.assertEqual(200,res_status,True)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()










