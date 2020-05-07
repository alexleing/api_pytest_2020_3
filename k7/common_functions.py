import requests
import re
import pytest
import os
# os.environ["host"] = "http://49.235.92.12:6009"
# host = os.environ["host"]
def login_fuc(s,username='admin',password='yoyo123456'):
    '''
    通用方法：登录
    :param s:
    :return: s这个对象即可
    '''
    url = os.environ["host"]+"/api/v1/login"
    body = {
        'username':username,
        'password':password
    }
    r = s.post(url, json=body)
    print(r.json())
    token = r.json()['token']
    print(token)
    h = {
        'Authorization': 'Token {}'.format(token),
        # 'Content-Type': 'application/json'
    }
    s.headers.update(h)
    return s


def get_info(s):
    url = os.environ["host"]+"/api/v1/userinfo"
    r = s.get(url)
    print(r.json())
    assert r.json()['msg'] == 'sucess!'
    return r.json()



def update_info(s, name='admin', mail='123@qq.com', sex='M',age=30):
    url = os.environ["host"]+"/api/v1/userinfo"
    body = {
        'name': name,
        'sex': sex,
        'age':age,
        'mail': mail
    }
    r =s.post(url, json=body)
    # print(r.json())
    return r.json()




if __name__ == '__main__':
    s = requests.session()
    login_fuc(s)
    get_info(s)
    infos = update_info(s, mail='283340479@qq.com')
    print(infos)