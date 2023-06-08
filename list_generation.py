# 列表生成式

# 生成有规律的列表

list1 = list(range(1, 11))
print(list1)

list2 = []
for i in range(1, 11):
    list2.append(i)
print(list2)

list3 = []
for i in range(1, 11):
    list3.append(i ** 2)
print(list3)

list4 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(list4)

list5 = [m + n for m in 'ABC' for n in 'XYZ']
print(list5)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
list6 = [k + "=" + v for k, v in d.items()]
print(list6)

L = ['Hello', 'World', 'IBM', 'Apple']
list7 = [s.lower() for s in L]
print(list7)

# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
#
# 提示：
#
# 1. isinstance(x, str) 可以判断变量 x 是否是字符串；
#
# 2. 字符串的 upper() 方法可以返回大写的字母。

L2 = ["hello", "world"]
list8 = [s.upper() for s in L2]
print(list8)
