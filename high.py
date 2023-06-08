# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-10, -11, abs))

