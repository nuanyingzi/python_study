# filter
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', 'B', None, ''])))


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n) == str(n[::-1])
