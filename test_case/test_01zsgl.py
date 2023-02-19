# 招商管理

import jsonpath
import unittest

from api.login_session import LoginSession
from conf.readConf import HandleIni


host_url = 'http://zzds.pythontest.aqara.com'

class zsgl(unittest.TestCase):

    def setUp(self, *args, **kw):
        self.sess = LoginSession()
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

    # 招商管理 - 招商信息：新增、查询
    def test_creat_zs(self):
        api_url = '/web/api/shang-join-information'
        url = self.host_url + api_url
        data ={
            "name": "AutoApiTest00004",      # 改下名字序号，逐次递增
            "phone": "15112340178",
            "work": "internet",
            "wechat": "wx00012",
            "email": "11112222@qq.com",
            "age": "18",
            "sex": "male",
            "education_id": 7,
            "connect_province_id": 1,
            "connect_city_id": 1,
            "connect_district_id": 17,
            "connect_address": "王府井大街3号店",
            "hometown": "北京",
            "shang_manager_id": {
                "activity_exception_icon": "",
                "display_name": "付招飞",
                "id": 8
            },
            "join_type_id": 17,
            "channel_id": 18,
            "intent_state": "strong",
            "first_will_province_id": 17,
            "first_will_city_id": 195,
            "first_will_district_id": 2068,
            "second_will_province_id": 1,
            "second_will_city_id": 1,
            "second_will_district_id": 19,
            "region_id": 170,
            "overall_rating": 5,
            "state": "pre_report",
            "focus_degree": "黄鹤楼",
            "funds_power": "归元寺",
            "work_exe": "光谷",
            "ides": "楚河汉界",
            "other": "大家基督教看到看到酷酷的",
            "distinguish": "shang"
        }
        resp = self.sess.login().post(url=url, json=data )
        #r_id = jsonpath.jsonpath(resp, "$[data][id]")  # 递归搜素key的写法
        #resp_json = resp.json()
        r_id = jsonpath.jsonpath(resp, "$..id")
        self.log.info("创建招商的ID：%s" % r_id)
        self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code,True)
        return r_id

    def test_query_zs(self):
        api_url = '/web/api/ui/views?view=shang-join-information-form&action=shang-join-information&res_ids={}'.format(self.test_creat_zs())
        url = self.HandleIni.host_url()+ api_url
        resp = self.sess.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code,True)

    # 招商管理 - 企业审核：查询、详情
    def test_query_company(self):
        api_url = '/web/api/shang-join-information/query?offset=0&limit=10&fields=[%22name%22,%22state%22,%22join_type_id%22,%22company_responsible%22,%22phone%22,%22regist_province_id%22,%22regist_city_id%22,%22regist_district_id%22,%22regist_address%22,%22company_count%22,%22regist_time%22,%22audit_time%22]&order=id%20desc&domains=[[%27distinguish%27,%20%27=%27,%20%27company%27]]'

        url = self.HandleIni.host_url() + api_url

        resp = self.sess.login().get(url=url)
        r_id = jsonpath.jsonpath(resp, "$..id")
        self.log.info("招商的ID：%s" % r_id)
        #self.log.info(resp.text)
        r_status_code = resp.status_code
        self.assertEqual(200,r_status_code,True)
        return r_id

    def test_query_zs(self):
        api_url = '/web/api/ui/views?view=shang_join_information_75&action=shang_join_information_24&res_ids={}'.format(self.test_query_company())

        url = self.HandleIni.host_url() + api_url
        resp = self.sess.login().get(url=url)
        # self.log.info(resp.text)
        r_status_code = resp.status_code
        print(r_status_code)
        self.assertEqual(200,r_status_code,True)

if __name__=="__main__":
    unittest.main()
