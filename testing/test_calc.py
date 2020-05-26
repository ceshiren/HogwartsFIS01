#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from python_code.calc import Calc
import yaml


def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


class TestCalc:

    def setup_class(self):
        print("setup_class")
        self.calc = Calc()

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("datas/data.yml")))
    # @pytest.mark.run(order=-1)
    def test_zadd_1(self, a, b, expect):
        result = self.calc.add(a, b)
        print(f"result = {result}")
        assert result == expect

    def get_steps(self):
        with open('steps/steps.yml') as f:
            return yaml.safe_load(f)

    def any_steps(self, data, expect):
        steps = self.get_steps()
        for step in steps:
            print(f"step == {step}")
            if 'add' == step:
                assert self.calc.add(*data) == expect
            elif 'add1' == step:
                assert self.calc.add1(data) == expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("datas/data.yml")))
    # @pytest.mark.run(order=-1)
    def test_zadd_2(self, a, b, expect):
        data = (a, b)
        self.any_steps(data, expect)
        # result1 = self.calc.add(*data)
        # assert result1 == expect
        #
        # result2 = self.calc.add1(data)
        # assert result2 == expect

    # @pytest.mark.first
    def test_sub(self):
        assert 1 == self.calc.sub(2, 1)

    # @pytest.mark.run(order=3)
    def test_mul(self):
        assert 6 == self.calc.mul(2, 3)

    # @pytest.mark.run(order=4)
    def test_div_1(self):
        result = self.calc.div(1, 1)
        print(f"result = {result}")
        assert result == 1


if __name__ == '__main__':
    pytest.main(['test_calc.py'])
