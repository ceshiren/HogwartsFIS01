#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
改造录制的用例：
第一次改造： 修改定位方式，将自动生成的xpath绝对定位，修改为可阅读的，可维护的定位方式
第二次改造： 使用pytest 测试框架
"""


class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        # caps['dontStopAppOnReset'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('username, gender, phonenum', [
        ('霍格沃兹学员5', '男', '13812345603'),
        ('霍格沃兹学员3', '女', '13812345601'),
        ('霍格沃兹学员4', '男', '13812345602'),
    ])
    def test_addcontact(self, username, gender, phonenum):
        # 点击 通讯录
        el1 = self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        el1.click()
        # 添加成员
        el2 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector()\
                                       .scrollable(true).instance(0)).\
                                       scrollIntoView(new UiSelector().\
                                       text("添加成员").instance(0));')
        el2.click()
        # 点击 手动输入添加
        el3 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手动输入' )]")
        el3.click()
        # 输入 姓名
        el4 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名' )]/..//*[contains(@class, 'EditText')]")
        el4.send_keys(username)
        # 选择性别
        # gender = '女'
        el5 = self.driver.find_element(MobileBy.XPATH, "//*[@text='男']")
        el5.click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        el7 = self.driver.find_element(MobileBy.XPATH,
                                       "//*[contains(@text, '手机') and contains(@class,'TextView')]/..//*[@text='手机号']")
        el7.send_keys(phonenum)
        el8 = self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']")
        el8.click()

        # print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
