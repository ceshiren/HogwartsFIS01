from selenium.webdriver.common.by import By
from test_selenium.test_wechat.page.add_member import AddMember
from test_selenium.test_wechat.page.base_page import BasePage
from test_selenium.test_wechat.page.contact import Contact


class Main(BasePage):

    def goto_add_member(self):
        # 点击跳转
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return Contact(self.driver)
