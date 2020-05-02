import requests
import re
import pytest


def login_fuc(s,username='admin',password='yoyo123456'):
    '''
    通用方法：登录
    :param s:
    :return: s这个对象即可
    '''
    url = 'http://49.235.92.12:8020/admin/login/?next=/admin/'

    # session  服务器根据csrf_token和其他的值生成一个session，该session需要和服务器里面的值进行比对
    r1 = s.get(url)

    # name='csrfmiddlewaretoken' value='QiqSi1M4SNnZXfzNTSfmRpesMsTrs8KY8HWuZfDZy8XoDgGH181pg5lienKSqK3k'
    # 使用正则表达式获取csrf_token的值，获取到的是一个列表，取第一个
    csrf_token = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r1.text)
    # print(csrf_token)
    print(csrf_token[0])

    body = {
        'csrfmiddlewaretoken':csrf_token[0],
        'username':username,
        'password':password,
        'next':'/admin/'
    }

    r2 = s.post(url, data=body)



    assert "站点管理 | Django 站点管理员" in r2.text
    cookie = s.cookies
    print(cookie)
    return  s
    # h = {
    #     'Cookie':cookie
    # }
    # 登录后的操作
def  add_user_info(s):
    '''
    添加用户的信息
    :return: 添加的结果断言
    '''
    url ='http://49.235.92.12:8020/admin/auth/user/add/'
    r = s.get(url)
    assert '增加 用户' in r.text
if __name__ == '__main__':
    s = requests.session()
    login_fuc(s)
    add_user_info(s)




