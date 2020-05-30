#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from app.page.app import App


class TestContactPO:

    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize('username, gender, phonenum', [
        ('霍格沃兹学员7', '男', '13812345607'),
        # ('霍格沃兹学员3', '女', '13812345601'),
        # ('霍格沃兹学员4', '男', '13812345602'),
    ])
    def test_addcontact(self, username, gender, phonenum):
        contactaddpage = self.main.goto_address().add_member().click_menualadd() \
            .set_name(username).set_gender(gender).set_phonenum(phonenum).click_save()
        contactaddpage.get_toast()
        # assert '添加成功' == tip
