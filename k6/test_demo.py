import pytest
import allure


@allure.feature("使用1个参数的设置")
@pytest.mark.parametrize("test_input,expected",
                         [
                             ("1+3",4),("11+3",14)
                         ])   # 如果使用的事一个参数，那么就要用字符串，不能使用元祖或者list
def test_eval(test_input,expected):
    a = test_input
    print('\n'+a)
    assert eval(a) == expected

# def test_eval_1():
#     a = "11+3"
#     assert eval(a) == 44