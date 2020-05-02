import requests
import json

base_url = 'http://apis.juhe.cn/simpleWeather/query'
parma = {
    'city':'上海',
    'key':'9385cc29148f3c9e576acf282c80bf5e '
}
a = requests.get(base_url, params=parma)
b = a.json()
c = a.status_code
d = a.headers
e = a.url
f = a.encoding
g = a.cookies

print(a, '\n', b, '\n', b['error_code'],c,d,e,f,g)
print(type(a))
print(g['aliyungf_tc'])
assert b['error_code'] == 0
# print(json.dumps(a.json(), indent=4, ensure_ascii=False))