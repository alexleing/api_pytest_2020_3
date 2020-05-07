# 快速生成列表
a = [i*i for i in range(10)]
print(a)
# 生成器
b = (i*i for i in range(10))
print(next(b))
print(next(b))