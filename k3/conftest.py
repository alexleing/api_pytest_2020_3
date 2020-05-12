import pytest
import requests
from k7.common_functions import login_fuc


'''
:arg scope: the scope for which this fixture is shared, one of
                ``"function"`` (default), ``"class"``, ``"module"``,
                ``"package"`` or ``"session"``.
'''
@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    login_fuc(s)
    yield  s
    print('后置操作')
    s.close()
    # return s

@pytest.fixture(scope="session")
def unlogin_fixture():
    print('\n不登录')
    s = requests.session()
    return s
