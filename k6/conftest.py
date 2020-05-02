import pytest
import requests
from k7.common_functions import login_fuc,update_info,get_info

'''
:arg scope: the scope for which this fixture is shared, one of
                ``"function"`` (default), ``"class"``, ``"module"``,
                ``"package"`` or ``"session"``.
'''
@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    login_fuc(s)
    if not s.headers.get('Authorization', ""):
         pytest.skip("登录未成功，跳过后面的用例")   #如果前置登录失败，那么使用该前置的用例全部都跳过
    yield  s
    print('后置操作')
    s.close()
    # return s

@pytest.fixture(scope="session")
def unlogin_fixture():
    print('\n不登录')
    s = requests.session()
    return s
