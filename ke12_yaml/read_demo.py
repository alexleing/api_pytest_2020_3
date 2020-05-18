import yaml

with open("demo.yml", "r", encoding="utf-8") as fp:
    t = fp.read()
print(t)

# 读取出来的字符串，转成dick

# b = ["a", "b", "c", "d"]
a = yaml.load(t)
print(a)

with open("demo_list.yml", "r", encoding="utf-8") as fp:
    x = fp.read()
b = yaml.load(x)
print(b)