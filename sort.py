l = [36, 5, -12, 9, -21]
l1 = sorted(l, key=abs)
print(l1)

str_list = ['bob', 'about', 'Zoo', 'Credit']
str_list1 = sorted(str_list, key=str.lower, reverse=True)
print(str_list1)


# 练习
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]


L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L1, key=by_name)
print(L2)
