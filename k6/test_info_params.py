from k7.common_functions import login_fuc,update_info,get_info
import requests
import pytest
from k6.read_yaml import get_yaml_data
import os


curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
yamlpath = os.path.join(curpath, 'update_info.yml')
print(yamlpath)
test_datas = get_yaml_data(yamlpath)
print(test_datas['test_info_params'])


@pytest.mark.skip('跳过的原因：有bug')
def test_2():
    '''已经知道该接口有bug'''
    print('已经知道该接口有bug')

# test_data = [
#                 ("M",{'message': 'update some data!', 'code': 0}),
#                 ("F",{'message': 'update some data!', 'code': 0}),
#                 ('X',{'message': '参数类型错误', 'code': 3333})
#
#             ]
# test_data = [
#     ("20",{'message': 'update some data!', 'code': 0}),
#     ("10",{'message': 'update some data!', 'code': 0}),
# ]

@pytest.mark.parametrize('age_input, age_expected', test_datas['test_age_params'])
@pytest.mark.parametrize('sex_input, expected',test_datas['test_info_params'],

                         ids=[
                             '测试修改个人信息sex=M',
                             '测试修改个人信息sex=F',
                             '测试修改个人信息sex=x,异常场景'
                         ])
def test_info_1(login_fixture, sex_input, expected, age_input, age_expected):
    '''测试修改个人信息的接口成功'''
    print('用例1')
    t = login_fixture
    print(t.headers)  # 头部有Authorization参数
    if not t.headers.get('Authorization', ""):
        pytest.skip("登录未成功，跳过后面的用例")

    r = update_info(t, sex=sex_input, age=age_input)
    print(r)
    assert r["message"] == expected['message']
    assert r["code"] == expected['code']

@pytest.mark.xxx
def test_3(login_fixture):
    print('xxx模块 自动化用例')

@pytest.mark.xxx
def test_4(login_fixture):
    print('xxx模块 自动化用例')


