# 门店管理：门店选址

import jsonpath
import unittest

from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni

# 门店管理：门店选址
class mdgl_mdxz(unittest.TestCase):

    def setUp(self, *args, **kw):
        self.sess = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()

    def tearDown(self):
        pass

    # def extract_jsonpath(json_obj, jpath):
    #     paths = jpath.split('.')
    #     for path in paths:
    #         if isinstance(json_obj, list):
    #             json_obj = json_obj[int(path)]
    #         else:
    #             json_obj = json_obj[path]
    #     return json_obj

    def test_creat_md(self):
        api_url = '/web/api/store-address'
        url = self.HandleIni.host_url()+api_url
        data ={
            "shang_info_id":489,
            "store_info_id":243,
            "urgency":"normal",
            "region_id":176,
            "shang_manager_id":100,
            "join_type_id":51,
            "affiliate_stage":"exam",
            "store_count":3,
            "credential":"[{\"userId\":16,\"userName\":\"\",\"uid\":\"93511875833689439834571716684813\",\"size\":4.98,\"name\":\"鹅鹅鹅.jpg\",\"type\":\"image/jpeg\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E9%B9%85%E9%B9%85%E9%B9%851640765406625.jpg\",\"key\":\"/ZZDS/鹅鹅鹅1640765406625.jpg\",\"rename\":\"鹅鹅鹅1640765406625.jpg\",\"extName\":\"jpg\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E9%B9%85%E9%B9%85%E9%B9%851640765406625.jpg\",\"createTime\":\"2021-12-29 16:10:06\"},{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"96535706115700406892950675954818\",\"size\":214.27,\"name\":\"哈哈哈.jpeg\",\"type\":\"image/jpeg\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E5%93%88%E5%93%88%E5%93%881640779440262.jpeg\",\"key\":\"/ZZDS/哈哈哈1640779440262.jpeg\",\"rename\":\"哈哈哈1640779440262.jpeg\",\"extName\":\"jpeg\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E5%93%88%E5%93%88%E5%93%881640779440262.jpeg\",\"createTime\":\"2021-12-29 20:04:03\"},{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"78994686589453320635213050543774\",\"size\":2908.71,\"name\":\"打印机指引.pdf\",\"type\":\"application/pdf\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951640779448617.pdf\",\"key\":\"/ZZDS/打印机指引1640779448617.pdf\",\"rename\":\"打印机指引1640779448617.pdf\",\"extName\":\"pdf\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951640779448617.pdf\",\"createTime\":\"2021-12-29 20:04:11\"}]",
            "enter_date":"2021-12-30 16:23:10",
            "phone":"17620315369",
            "warranty_state":"paid",
            "expect_region_province_id":31,
            "expect_region_city_id":383,
            "expect_region_district_id":3775,
            "tenant_range_id":4,
            "requirement":"就大家的积极等级"
        }

        resp = self.Zzds.login().post(url=url, json=data)
        #r_id = jsonpath.jsonpath(resp, "$[data][id]")  # 递归搜素key的写法
        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")
        self.log.info("创建招商的ID：%s" % r_id)
        self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code,True)
        return r_id

    def test_query_md(self):
        api_url = '/web/api/ui/views?view=store_address_52&action=store_address_17&res_ids={}'.format(self.test_creat_md())
        url = self.HandleIni.host_url()+api_url
        resp = self.Zzds.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code,True)


    # 门店管理：门店信息
    def test_creat_md(self):
        api_url = '/web/api/store-address'
        url = self.HandleIni.host_url() + api_url
        data ={
            "shang_info_id":489,
            "store_info_id":243,
            "urgency":"normal",
            "region_id":176,
            "shang_manager_id":100,
            "join_type_id":51,
            "affiliate_stage":"exam",
            "store_count":3,
            "credential":"[{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"93511875833689439834571716684813\",\"size\":4.98,\"name\":\"鹅鹅鹅.jpg\",\"type\":\"image/jpeg\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E9%B9%85%E9%B9%85%E9%B9%851640765406625.jpg\",\"key\":\"/ZZDS/鹅鹅鹅1640765406625.jpg\",\"rename\":\"鹅鹅鹅1640765406625.jpg\",\"extName\":\"jpg\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E9%B9%85%E9%B9%85%E9%B9%851640765406625.jpg\",\"createTime\":\"2021-12-29 16:10:06\"},{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"96535706115700406892950675954818\",\"size\":214.27,\"name\":\"哈哈哈.jpeg\",\"type\":\"image/jpeg\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E5%93%88%E5%93%88%E5%93%881640779440262.jpeg\",\"key\":\"/ZZDS/哈哈哈1640779440262.jpeg\",\"rename\":\"哈哈哈1640779440262.jpeg\",\"extName\":\"jpeg\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E5%93%88%E5%93%88%E5%93%881640779440262.jpeg\",\"createTime\":\"2021-12-29 20:04:03\"},{\"userId\":16,\"userName\":\"冯加刚\",\"uid\":\"78994686589453320635213050543774\",\"size\":2908.71,\"name\":\"打印机指引.pdf\",\"type\":\"application/pdf\",\"status\":\"done\",\"url\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951640779448617.pdf\",\"key\":\"/ZZDS/打印机指引1640779448617.pdf\",\"rename\":\"打印机指引1640779448617.pdf\",\"extName\":\"pdf\",\"thumbnailUrl\":\"http://test-scf-cos-1300889962.cos.ap-guangzhou.myqcloud.com/ZZDS/%E6%89%93%E5%8D%B0%E6%9C%BA%E6%8C%87%E5%BC%951640779448617.pdf\",\"createTime\":\"2021-12-29 20:04:11\"}]",
            "enter_date":"2021-12-30 16:23:10",
            "phone":"17620315369",
            "warranty_state":"paid",
            "expect_region_province_id":31,
            "expect_region_city_id":383,
            "expect_region_district_id":3775,
            "tenant_range_id":4,
            "requirement":"就大家的积极等级"
        }

        resp = self.Zzds.login().post(url=url, json=data )
        #r_id = jsonpath.jsonpath(resp, "$[data][id]")  # 递归搜素key的写法
        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")
        self.log.info("创建招商的ID：%s" % r_id)
        self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code)
        return r_id

    def test_query_md(self):
        api_url = '/web/api/ui/views?view=store_information_168&action=store_information_19&res_ids={}'.format(self.test_creat_md())
        url = self.HandleIni.host_url()+api_url
        resp = self.Zzds.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code)


    # 门店管理 - 门店设计：分配设计师
    def test_distribution(self):
        api_url = '/web/api/store-design-distribution'
        url = self.HandleIni.host_url()+api_url
        data = {'designer': '冯大设计师'}
        resp = self.Zzds.login().post(url=url,json=data)
        r_status_code = resp.status_code
        self.assertEqual(200, r_status_code, True)
        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")
        return r_id


    # 门店管理 - 门店装修：分配监理
    def test_distribution(self):
        api_url = '/web/api/store-design-distribution'
        url = self.HandleIni.host_url()+api_url
        data = {'supervision_responsible_id': '16'}
        resp = self.Zzds.login().post(url=url,json=data)
        r_status_code = resp.status_code
        self.assertEqual(200, r_status_code, True)
        resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp_json, "$..id")
        return r_id

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()

