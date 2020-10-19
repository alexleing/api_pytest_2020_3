import re
# import  requests
# def login_fuc(s,username='admin',password='yoyo123456'):
#     url = 'http://49.235.92.12:6009/api/v1/login'
#     body = {
#         'username':username,
#         'password':password
#     }
#     r = s.post(url, json=body)
#     print(r.json())
#     token = r.json()['token']
#     h = {
#         'Authorization': 'Token {}'.format(token)
#     }
#     s.headers.update(h)
#     return s
#
# if __name__ == '__main__':
#     s = requests.session()
#     r = login_fuc(s)
# [3, 5, 1, 7]  [1,3,5] [3,5,1]
# a = [1, 3, 5, 7]
# b = a[0:3]
# c = b[1:3]
# d = b[:1]
# e = c+d
# h = a[-1:]
# i = e+h
# b =a[1:]
# c = a[:1]
# print(a,b,c,d,e,h,i)
# a = 'hello'
# b = list(a)
# f = ''.join(b)
# print(b,f)
# c = a[:4]
# d = a[-1:]
# e = d+c
# print(a, e, f)
#

i = 1
j = 0
res = []
for a in range(201):
    number = i + j
    i = j
    j = number
    if number > 200:
        break
    else:
        # print(number)
        res.append(number)

print(res)

# a="hello_world_yoyo"
# b =a.split("_")
# print(type(b),b)
# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# print("列表a的长度是：%d" % len(a))
# b = []
# c = []
# d = []
# for i in a:
#     if i > 0:
#         b.append(i)
#     elif i < 0:
#         c.append(i)
#     else:
#         d.append(i)
# print("列表a包含正数的数量是：%d" %len(b))
# print("列表a包含正数的数量是：{data}".format(data=len(c)))
# print("列表a包含数字0，数量是：%d" % len(d))
# while True:
#     email = input("请输入邮箱:")
#     if email.upper() == "Q":
#         break
#     res = re.findall(".com$", email)
#     if not res:
#         print("incorrect email format")
#     temp = email.split("@")
#     name = temp[0]
#     com = temp[1].split(".")[0]
#     print(f"用户名:{name} , 公司名:{com}")


# a = [1, 3, -3, 4, -2, 8, -7, 6]
# b = []
# # c = []
# for i in a:
#     if i > 0:
#         b.append(i)
#     # else:
#     #     c.append(i)
# print(b)
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
#
# c = [str(x)+str(y) for x, y in zip(b, a)]
# print(c)

# L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
# print(list(set(L)))
#
# L1 = [1, 2, 3, 4, 5]
# print(L1[10:])


a = [i*i for i in range(1,10)]
print(a)

def sum_demo(x, y):
    result = 0
    for _ in range(2):
        x +=1
        y +=1
        result = x + y
    return result

if __name__ == '__main__':
    result = sum_demo(1, 1)
    print(result)



