def sq(x):
    return x * x


List = [1, 2, 3, 4, 5, 6]
xx = map(sq, List)
l1 = list(xx)
print(l1)

ss = map(str, List)
l2 = list(ss)
print(l2)


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    def toUpperStr(str):
        return str.capitalize()
    res = map(toUpperStr, name)
    return list(res)


LL = normalize(['adam', 'LISA', 'barT'])
print(LL)


