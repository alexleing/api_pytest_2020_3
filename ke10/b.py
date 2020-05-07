

def func(a=10):
    while True:
        a = a+2
        yield a+2

b = func(a=10)
print(next(b))
print(next(b))