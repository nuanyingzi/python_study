# f = open('D:/Code/python/python_study/test.txt', 'r')
# txt = f.read()
# print(txt)
# f.close()


# 2
# try:
#     f = open('D:/Code/python/python_study/test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


# 3
# with open('D:/Code/python/python_study/test.txt', 'r', encoding='gbk', errors='ignore') as f:
#     for line in f.readlines():
#         print(line.strip())


# 图片 视频 使用rb模式读取
# with open('D:/Code/python/python_study/qin.jpg', 'rb') as p:
#     print(p.read())

with open('D:/Code/python/python_study/test.txt', 'a') as f:
    f.write('Hello world!')

