#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.base import BasePage
from app.page.invitemember import InviteMemberPage


class AddressListPage(BasePage):

    def add_member(self):
        el2 = self.find(MobileBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector()\
                        .scrollable(true).instance(0)).\
                        scrollIntoView(new UiSelector().\
                        text("添加成员").instance(0));')
        el2.click()
        return InviteMemberPage(self._driver)
