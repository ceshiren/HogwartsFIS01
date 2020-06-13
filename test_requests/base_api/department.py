import requests

from test_requests.base_api.wework import WeWork


class Department(WeWork):

    def create_department(self, name, name_en, c_id,parentid=1, order=1):
        req = {
        "method":"post",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
        "params": {"access_token": self.token},
        "json": {"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": c_id}
        }
        r = self.send_api(req)
        return r

    def update_department(self, name, name_en, c_id,parentid=1, order=1):
        req = {
        "method":"post",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
        "params": {"access_token": self.token},
        "json": {"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": c_id}
        }
        r = self.send_api(req)
        print(r)
        return r

    def delete_department(self, c_id):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {"access_token": self.token, "id": c_id},
        }
        r = self.send_api(req)
        return r

    def getlist_department(self):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {
                "access_token": self.token,
            }
        }
        r = self.send_api(req)
        print(r)
        return r