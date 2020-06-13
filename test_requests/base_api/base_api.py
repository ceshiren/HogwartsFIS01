import requests
import yaml


class BaseApi:

    def send_api(self, req):
        """
        1. 先把请求信息转为为一个json结构体
        2. 在base_api里面对requests.request进行封装
        3. 传入为json结构体的请求信息，给requests.request，
        使用关键字传参的方式传入的时候要注意解包
        :param req: 一个json结构体的请求信息
        :return:
        """
        # 两个** 代表对字典进行解包， 使用 k=v 的形式进行传参
        return requests.request(**req).json()

    def yaml_load(self, file):
        return yaml.safe_load(open(file))
