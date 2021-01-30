import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_datas = datas_add['datas']
    print(add_datas)
    add_myid = datas_add['myid']
    print(add_myid)

    # datas = yaml.safe_load(f)
    datas_div = datas['div']
    div_datas = datas_div['datas']
    print(div_datas)
    div_myid = datas_div['myid']
    print(div_myid)


# def test_a():
#     print("a")


# def func():
class TestCalc:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=add_myid

    )
    def test_add(self, a, b, expect):
        # 实例化计算器的类
        # calc = Calculator()
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 判断result 是浮点数，保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 断言
            assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas, ids=div_myid
    )
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)

            assert result == expect

    # def test_add2(self):
    #     result = self.calc.add(0.1, 0.2)
    #     assert round(result, 2) == 0.3

    # def test_add1(self):
    #     #实例化计算器的类
    #     # calc = Calculator()
    #     #调用 add 方法
    #     result = self.calc.add(0.1, 0.1)
    #     #断言
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     #实例化计算器的类
    #     # calc = Calculator()
    #     #调用 add 方法
    #     result = self.calc.add(-1, -1)
    #     #断言
    #     assert result == -2


