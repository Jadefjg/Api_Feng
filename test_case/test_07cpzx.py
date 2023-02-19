
# 产品中心

import unittest
import jsonpath
from api.login_session import LoginSess
from test_tools.handle_log import Log
from conf.readConf import HandleIni


class Cpzx(unittest.TestCase):

    def setUp(self):
        self.sess = LoginSess()
        self.log = Log()
        self.HandleIni = HandleIni()

    # 产品信息
    def test_query(self):
        """获取产品信息id"""
        api_url = '/web/api/dim-product-sku/query?offset=0&limit=10&fields=[%22spu_id%22,%22mdm_code%22,%22spu_name%22,%22state%22,%22specification%22,%22icon%22,%22product_category_id%22,%22hardware_model_no%22,%22product_brand_id%22,%22barcode%22,%22product_attribute_id%22,%22material_code%22]&order=id%20desc&domains=[]'
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        resp = res.json()
        r_id = jsonpath.jsonpath(resp,"$..id")[0]
        print(r_id)
        return r_id

    def test_details(self):
        """产品信息的详情"""
        api_url = "/web/api/ui/views?view=dim_product_sku_148&action=dim_product_sku_34&res_ids={}".format(self.details())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        res_code = res.status_code
        self.assertEqual(200,res_code,True)

    # 产品品牌
    def test_querypq(self):
        """获取产品品牌id"""
        api_url = '/web/api/dim-product-product-brand/query?offset=0&limit=10&fields=[%22name%22]&order=id%20desc&domains=[]'
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        resp = res.json()
        r_id = jsonpath.jsonpath(resp,"$..id")[0]
        print(r_id)
        return r_id

    def test_detailspq(self):
        """产品品牌的详情"""
        api_url = "/web/api/ui/views?view=dim_product_product_brand_71&action=dim_product_product_brand_21&res_ids={}".format(self.detailspq())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        res_code = res.status_code
        self.assertEqual(200,res_code,True)

    # 产品属性
    def test_create_attbu(self):
        """新增产品属性"""
        api_url = "/web/api/dim-product-product-attribute"
        url = self.HandleIni.host_url() + api_url
        data = {"name":"下课时刻dhhd","state":"disable"}
        res = self.sess.login().post(url=url,json=data)
        self.assertEqual(200,res.status_code,True)

        res_json = res.json()
        r_id = jsonpath.jsonpath(res_json,"$..id")
        return r_id

    def test_detail01(self):
        api_url = "/web/api/ui/views?view=dim_product_product_attribute_177&action=dim_product_product_attribute_35&res_ids={}".format(self.test_detail01())
        url = self.HandleIni.host_url() + api_url
        res = self.sess.login().get(url=url)
        self.assertEqual(200,res.status_code,True)

    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()





