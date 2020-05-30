import os

from selenium import webdriver
import time
import json

# test2233
from selenium.webdriver.common.by import By


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def test_get_cookie(self):
        """
        获取cookie
        :return:
        """

        time.sleep(10)
        cookie = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            # 将cookie存入一个json文件中
            json.dump(obj=cookie, fp=f)

    def test_cookie_login(self):
        cookies = json.load(open("./cookie.json"))
        # 循环cookies列表，将所有cookie添加到浏览器中
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            ## 只添加一个cookie
            self.driver.add_cookie(cookie)
        time.sleep(2)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # dir 获取的就是当前文件的绝对路径
        dir = os.path.dirname(__file__)
        print(__file__)
        print(dir)
        # 上传文件，上传文件可以使用send_keys。前提元素的标签必须为input。
        # send_keys里面放的文件，必须是绝对路径
        time.sleep(2)
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(dir + "/data.xlsx")

        ele_name = self.driver.find_element(By.ID, "upload_file_name").text
        # 断言上传文件的名称
        assert ele_name == "data111.xlsx"
