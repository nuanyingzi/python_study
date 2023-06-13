# 文件与目录
import os.path

l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)

l2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l2)

