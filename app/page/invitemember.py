#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from app.page.contactadd import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy

from app.page.base import BasePage


class InviteMemberPage(BasePage):

    def click_menualadd(self):
        from app.page.contactadd import ContactAddPage
        el3 = self.find(MobileBy.XPATH, "//*[contains(@text,'手动输入' )]")
        el3.click()

        return ContactAddPage(self._driver)

    def get_toast(self):
        print(self._driver.page_source)
        self.find(MobileBy.XPATH, "//*[@text='添加成功']").click()
