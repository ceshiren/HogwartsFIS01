from test_selenium.test_wechat.page.main import Main


class TestContactButton:
    def setup(self):
        self.main = Main()

    def test_contact_button(self):
        self.main.goto_contact().click_button()

    def teardown(self):
        self.main.quit()
