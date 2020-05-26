import hashlib

key = "12345678"

# body = {
#     "username": "test",
#     "password": "123456",
#     "mail": "",
#     "sign": "xxxx"
# }
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
if __name__ == '__main__':
    body = {
        "username": "test",
        "password": "123456",
        "mail": "",
        "sign": "xxxx"
    }
    sign = sign_body(body, key="12345678")
    print(sign)


