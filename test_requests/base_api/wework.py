import yaml

from test_requests.base_api.base_api import BaseApi


class WeWork(BaseApi):

    def get_token(self, corpsecret):
        corpid = "ww93348658d7c66ef4"
        req = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params" : {"corpid": corpid, "corpsecret": corpsecret}
        }
        r = self.send_api(req)
        self.token = r["access_token"]
        return self.token

