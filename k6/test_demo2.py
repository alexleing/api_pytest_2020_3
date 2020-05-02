import  pytest

# 期望结果都是固定的一个
# username "", 123, "aaaaaa"
# psw "", 234, "bbb"
@pytest.mark.parametrize("pwd",["", 234, "bbb"])
@pytest.mark.parametrize("username",["", 123, "aaaaaa"])   # 如果使用的事一个参数，那么就要用字符串，不能使用元祖或者list
def test_eval(username,pwd):
    print("\n账号和密码的组合：{username}，{pwd}".format(username=username, pwd=pwd))

