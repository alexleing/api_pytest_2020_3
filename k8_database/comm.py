import requests


def register(s,username="test1234455q",
             password="123456",
             mail="test1123@qq.com"):

    url = "http://49.235.92.12:6009/api/v1/register"

    body = {
        "username":username,
        "password":password,
        "mail": mail
    }
    r = s.post(url, json=body)
    # print(r.text)
    # print(r.json())
    return r

if __name__ =='__main__':
    s = requests.session()
    r = register(s,username='testhahaha1',
                 password='123456',
                 mail='testrjsdfjsd@qq.com')
    print(r.json())

