from k7.common_functions import login_fuc,update_info,get_info
import requests
import  pytest
# s = requests.session()
def test_info_1(login_fixture):
    '''成功'''
    print('用例1')
    t = login_fixture
    r = update_info(t)
    assert r['message'] == 'update some data!'
    return r


def test_info_2(unlogin_fixture):
    '''成功2'''
    print('用例2')
    s = unlogin_fixture
    print(s.headers)

def test_info_3(login_fixture):
    '''成功3'''
    print('用例3')
    s = login_fixture
    r = get_info(s)



