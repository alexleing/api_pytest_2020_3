import requests
import pytest


def test_joke_1(key1):
    url = "http://japi.juhe.cn/joke/content/text.from"
    params = {
        'key': key1,
        'page': 1,
        'pagesize': 2
    }
    r = requests.get(url, params=params)
    print(r.json())
    assert r.json()['reason'] == 'Success'
def test_joke_2(key1):
    url = "http://japi.juhe.cn/joke/content/text.from"
    params = {
        'key': key1,
        'page': 1,
        'pagesize': 2
    }
    r = requests.get(url, params=params)
    print(r.json())
    assert r.json()['reason'] == '错误的请求KEY'

def test_joke_3(key1):
    url = "http://japi.juhe.cn/joke/content/text.from"
    params = {
        'key': key1,
        'page': 1,
        'pagesize': 2
    }
    r = requests.get(url, params=params)
    print(r.json())
    assert r.json()['reason'] == '错误的请求KEY'



# if __name__ == '__main__':
#     test_joke_1(key1='61453cf60a746632636b89647c779d32')
#     test_joke_2(key1='')
#     test_joke_3(key1='61453cf6')




