# x的n次方
def square(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(square(9, 3))
