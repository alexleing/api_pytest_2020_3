from k8_database.comm import register
import pytest
from connet_mysql import execute_sql

@pytest.fixture()
def delete_register():
    '''执行SQL删除注册'''
    sql = 'DELETE from auth_user where username = "test1234455q";'
    execute_sql(sql)

def test_register_1(unlogin_fixture,delete_register):
    '''测试用例：注册'''
    s = unlogin_fixture
    r = register(s)
    print(r.json())


def test_register_2(unlogin_fixture,delete_register):
    '''测试用例：重复注册'''
    s = unlogin_fixture
    r = register(s)
    r1 = register(s)
    print(r1.json())
    # assert r.json()['msg'] == '注册成功!'
    assert '用户已被注册'in r1.json()['msg']
