# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2 +bx+c=0 的两个解。
import math


def quadratic(a, b, c):
    if all(isinstance(a, (int, float)) for x in (a, b, c)):
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / 2 * a
            x2 = (-b - math.sqrt(delta)) / 2 * a
            return x1, x2
        else:
            raise TypeError('wujie')
    else:
        raise TypeError('bad operand type')


x, y = quadratic(5, 8, 9)
print(x, y)
