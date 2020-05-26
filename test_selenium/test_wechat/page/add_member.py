import time

from selenium.webdriver.common.by import By

from test_selenium.test_wechat.page.base_page import BasePage
from test_selenium.test_wechat.page.contact import Contact


class AddMember(BasePage):
    _ele_username = "username"

    def add_member(self):
        time.sleep(3)
        # 姓名
        self.find(By.ID, self._ele_username).send_keys("庄周u")
        # 账号
        self.find(By.ID, "memberAdd_acctid").send_keys("9882212")
        # 手机号
        self.find(By.ID, "memberAdd_phone").send_keys("19211122213")
        # 点击保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)

    def add_member_fail(self):
        # 姓名
        self.find(By.ID, self._ele_username).send_keys("阿英")
        # 账号
        self.find(By.ID, "memberAdd_acctid").send_keys("9010978")
        # 手机号
        self.find(By.ID, "memberAdd_phone").send_keys("19911112229")
        # 点击保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)
