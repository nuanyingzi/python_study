from functools import reduce

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

L = list(range(1, 11, 2))


def f(x, y):
    return x * 10 + y


list1 = reduce(f, L)
print(list1)


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2int(str):  # 整合到一个函数
    return reduce(fn, map(char2num, str))


s = '1234567'
str2 = str2int(s)
print(str2)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(str):
    pass
