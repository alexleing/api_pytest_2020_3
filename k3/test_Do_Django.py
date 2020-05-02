import requests
from k3.test_login import login_fuc

s = requests.session()

def test_get_info(login_fixture):

    url ='http://49.235.92.12:8020/admin/auth/user/add/'
    r = s.get(url)
    assert '增加 用户' in r.text


