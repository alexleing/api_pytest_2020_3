import hashlib


def setup_hook():
    print("用例开始之前")

def tear_down():
    print("用例结束后")

def sign_body(body, key="12345678"):
    a = body.items()
    print(a)
    print(type(a))

    b = ["".join(i)for i in a if i[1] and i[0] != "sign"]
    print(b)
    b.sort()
    print(b)
    c = "".join(b)
    print(c)
    new_str = c + key
    print(new_str)

    # md5加密

    m = hashlib.md5()
    m.update(new_str.encode("utf-8"))
    return m.hexdigest()

def setup_sign(request):
    body = request["json"]
    print("body内容：%s"%body) # dict
    sign = sign_body(body, key="12345678")

    body["sign"] = sign