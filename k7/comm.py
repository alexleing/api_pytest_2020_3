import  requests


def com_f(key):
    url = "http://japi.juhe.cn/joke/content/text.from"
    params = {
        'key': key,
        'page': 1,
        'pagesize': 2
    }
    r = requests.get(url, params=params)
    print(r.json())
    return r