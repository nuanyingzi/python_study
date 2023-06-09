# 闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


s = lazy_sum(1, 2, 3)
ss = s()
print(ss)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2
