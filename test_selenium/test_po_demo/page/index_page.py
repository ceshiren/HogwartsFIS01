from test_selenium.test_po_demo.page.login_page import LoginPage
from test_selenium.test_po_demo.page.register_page import RegisterPage


class IndexPage:

    def goto_register(self):
        # 点击行为，点击之后跳转到注册页面
        # driver.find_element(by.id, "xxx").click()
        return RegisterPage()

    def goto_login(self):
        # 点击行为，点击之后跳转到登录页面
        # driver.find_element(by.id, "xxx").click()
        return LoginPage()

    def goto_download(self):
        pass
