# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

r = 'D:/Code/python/python_study'  # 目录
for name in os.listdir(r):
    print(name)
