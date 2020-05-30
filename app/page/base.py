#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = [
        (MobileBy.XPATH, '//*[@text="下次再说"]'),
        (MobileBy.XPATH, '//*[@text="确定"]'),
    ]
    _max_errornum = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            self._error_num = 0
            return element
        except Exception as e:
            if self._error_num > self._max_errornum:
                raise e
            self._error_num += 1

            for ele in self._black_list:
                ellist = self._driver.find_elements(*ele)
                if len(ellist) > 0:
                    ellist[0].click()
                    return self.find(locator, value)
            raise e
