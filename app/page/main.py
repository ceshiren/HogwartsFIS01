#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist import AddressListPage
from app.page.base import BasePage


class Main(BasePage):

    def goto_message(self):
        pass

    def goto_address(self):
        # 进入 通讯录
        el1 = self.find(MobileBy.XPATH, "//*[@text='通讯录']")
        el1.click()
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
