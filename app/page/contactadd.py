#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.base import BasePage


class ContactAddPage(BasePage):

    def set_name(self, username):
        # 输入用户名
        el4 = self.find(MobileBy.XPATH, "//*[contains(@text,'姓名' )]/..//*[contains(@class, 'EditText')]")
        el4.send_keys(username)

        return self

    def set_gender(self, gender):
        # 选择性别
        # gender = '女'
        el5 = self.find(MobileBy.XPATH, "//*[@text='男']")
        el5.click()
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        return self

    def set_phonenum(self, phonenum):
        el7 = self.find(MobileBy.XPATH,
                        "//*[contains(@text, '手机') and contains(@class,'TextView')]/..//*[@text='手机号']")
        el7.send_keys(phonenum)
        return self

    def click_save(self):
        from app.page.invitemember import InviteMemberPage
        el8 = self.find(MobileBy.XPATH, "//*[@text='保存']")
        el8.click()

        return InviteMemberPage(self._driver)
