import pytest
from ke11.common_function import add_xx, modify_xx, get_xx
import allure


@allure.feature("模块1：1111")
def test_01():
    '''用例一的描述'''
    print("测试用例1")
@allure.feature("模块1：1111")
@allure.issue("url","这里填写描述")
def test_02():
    '''用例一的描述'''
    print("测试用例2")

@allure.feature("模块2：22222")
@allure.story("story为用例的标题：这里是用例的标题")
@allure.testcase("url:这里填写用例对应的功能用例地址")
def test_03(login_fixture1):
    '''用例三的描述'''
    # print("测试步骤1：")
    add_xx()
    # print("测试步骤2：")
    modify_xx()
    # print("测试步骤3：")
    get_xx()