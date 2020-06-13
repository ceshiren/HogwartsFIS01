import json

from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate

from test_requests.base_api.department import Department


class TestDepartment:
    ## token只需要每个用例集之前执行一次，不需要重复获取
    def setup_class(self):
        self.department = Department()
        self.token = self.department.get_token(self.department.yaml_load("config.yml")["contact"])

    def test_create_department(self):
        r = self.department.create_department("旺仔牛奶2号","numwz2",1001)
        assert r["errcode"] == 0

    def test_update_department(self):
        r = self.department.update_department("旺仔牛奶2号","numwz2",1001)
        schema = json.load(open("schema.json"))
        validate(r, schema)
        assert r["errmsg"] == 'updated'


    def test_delete_department(self):
        r = self.department.delete_department(1001)
        assert r["errcode"] == 0

    def test_getlist_department(self):
        r = self.department.getlist_department()
        # json的格式化工具，打印带格式，好看
        # print(json.dumps(r, indent=2, ensure_ascii=False))
        # from jsonpath import jsonpath
        res = jsonpath(r, "$.department[?(@.id==2)]")[0]
        print(res)
        assert r["errcode"] == 0
        assert_that(res, has_value("广州研发中心"), reason="匹配失败")





