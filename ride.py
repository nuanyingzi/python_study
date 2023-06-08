# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def mul(x, y, **kw):
    s = x * y
    for k in kw:
        s = s * k
    return s
ss = mul(1, 2, 45, 6)
print(ss)
