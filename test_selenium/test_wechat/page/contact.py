import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_wechat.page.base_page import BasePage


class Contact(BasePage):

    def click_button(self):
        ele = (By.CSS_SELECTOR, ".ww_checkbox")
        self.waitfor_click(ele)
        self.find(By.CSS_SELECTOR, ".ww_checkbox").click()

    def get_member(self):
        """
        得到所有的成员信息
        :return:
        """
        ## 这个列表存放所有的名单信息
        list1 = []
        while True:
            # 获取翻页,meassage获取到的是一个 1/3, 2/3, 3/3/3
            time.sleep(1)
            meassage: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            # 得到当前页和总页数，切割后是["1","3"]所以需要强转
            print(meassage)
            cur_page, total_page = [int(i) for i in meassage.split("/", 1)]

            member_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            # 把列表中的姓名拿出来
            for ele in member_list:
                list1.append(ele.get_attribute("title"))
            # cur_page = [int(i) for i in meassage.split("/",1)][0]
            if cur_page == total_page:
                print(list1)
                return list1

            self.find(By.CSS_SELECTOR, ".js_next_page").click()
