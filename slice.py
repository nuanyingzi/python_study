# 切片
L = list(range(100))
print(L[::5])

T = (0, 1, 2, 3, 4, 5)
print(T[0:3])

S = 'ABCDEFG'
print(S[::2])


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    n = 0
    m = len(s)
    while n < m and s[n] == ' ':
        n = n + 1
    while n < m and s[m-1] == ' ':
        m = m - 1
    return s[n:m]

print(trim("   sdagdy   ashh  s  --- "))
