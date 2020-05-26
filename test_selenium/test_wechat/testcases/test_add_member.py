from test_selenium.test_wechat.page.main import Main


class TestAddMember:

    def test_add_member(self):
        main = Main()
        assert "庄周" in main.goto_add_member().add_member().get_member()

    def test_add_member_fail(self):
        main = Main()
        assert "阿英" not in main.goto_add_member().add_member_fail().get_member()
