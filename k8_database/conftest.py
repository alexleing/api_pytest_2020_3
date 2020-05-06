import pytest
import requests
from connet_mysql import execute_sql
@pytest.fixture()
def unlogin_fixture():
    '''不登录'''
    s = requests.session()
    return s

@pytest.fixture()
def delete_register():
    '''执行SQL删除注册'''
    sql = 'DELETE from auth_user where username = "test1234455q";'
    execute_sql(sql)
