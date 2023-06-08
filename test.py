# 比如构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现

def su():
    n = 0
    li = []
    while n < 100:
        n = n + 1
        if n % 2 == 0:
            continue
        li.append(n)
    return li

print(su())
