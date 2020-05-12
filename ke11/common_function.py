import allure

@allure.step("登录")
def login():
    print("先登录")

@allure.step("添加xx内容")
def  add_xx():
    print("添加xx内容")

@allure.step("修改xx内容")
def  modify_xx():
    print("修改xx内容")

@allure.step("查询xx内容")
def  get_xx():
    print("查询xx内容")