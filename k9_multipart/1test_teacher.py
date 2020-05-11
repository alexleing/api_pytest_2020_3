from k9_multipart.login_xmind import  login_fuc
from k9_multipart.form_data import add_teacher_name
import requests
import pytest
from connet_mysql import select_sql, execute_sql


@pytest.fixture()
def delete_teacher():
    sql = "delete  from djangoweb.hello_teacher where teacher_name = 'testhahaah123235'"
    execute_sql(sql)
    yield
    execute_sql(sql)

def test_add_teacher(delete_teacher):
    s = requests.session()
    login_fuc(s)
    text = add_teacher_name(s)
    sql = "select count(*) as sum from djangoweb.hello_teacher where teacher_name = 'testhahaah123235';"
    result1 = select_sql(sql)[0]['sum']
    print(result1)
    assert  result1 == 1
