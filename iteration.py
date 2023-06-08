# 迭代

for k, v in enumerate(["A", "B", "C"]):
    print(k, v)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if isinstance(L, list):
        if not L:
            return None, None
        minNum = L[0]
        maxNum = L[0]
        for i in L:
            if i < minNum:
                minNum = i
            if i > maxNum:
                maxNum = i
        return minNum, maxNum
    else:
        return None, None


ssss = findMinAndMax([])
print(ssss)
