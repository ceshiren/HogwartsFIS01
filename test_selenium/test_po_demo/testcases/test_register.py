from test_selenium.test_po_demo.page.index_page import IndexPage


class TestRegister:
    def test_login_register(self):
        index = IndexPage()
        # 1. 点击登录进入登录页面，
        # 2. 点击立即注册，进入注册页面，
        # 3. 开始注册
        index.goto_register().register()
        index.goto_login().goto_register().register()
