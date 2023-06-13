# 练习
# 利用os模块编写一个能实现dir -l输出的程序。
# 已知dir -l获取的格式如下：
# 2023/06/13  14:36    <DIR>          .
# 2023/06/13  14:36    <DIR>          ..
# 2023/06/02  17:25             6,359 .bash_history
# 2023/01/04  15:40    <DIR>          .config
# 2023/01/06  16:33    <DIR>          .dlv
# 2023/06/01  10:05    <DIR>          .docker
# 2023/06/12  10:00               202 .gitconfig
# 2023/05/18  17:24                20 .lesshst
# 2023/03/28  14:37                42 .npmrc
# 2023/05/18  16:12    <DIR>          .ssh
# 2023/02/17  09:51    <DIR>          .VirtualBox
# 2023/06/13  14:36    <DIR>          .vscode
# 2023/03/28  14:40                32 .vuerc
# 2023/03/31  15:32               121 .yarnrc
# 2022/07/26  16:59    <DIR>          3D Objects
# 2022/07/26  16:59    <DIR>          Contacts
# 2023/06/02  10:43    <DIR>          Creative Cloud Files
# 2023/06/12  09:00    <DIR>          Desktop
# 2023/06/08  09:40    <DIR>          Documents
# 2023/06/12  09:03    <DIR>          Downloads
# 2022/07/26  16:59    <DIR>          Favorites
# 2023/01/02  15:31    <DIR>          go
# 2022/07/26  16:59    <DIR>          Links
# 8 个文件          7,412 字节
#               24 个目录 56,954,150,912 可用字节
import os
import time

filenum, dirnum, fsize = 0, 0, 0
r = 'D:/Code/python/python_study'
for name in os.listdir(r):
    if os.path.isfile(name):
        filenum += 1
        fsize += os.path.getsize(name)
        print('%s\t\t\t%d\t%s' % (time.strftime("%Y/%m/%d %H:%M", time.localtime(os.path.getmtime(name))), os.path.getsize(name), name))
    if os.path.isdir(name):
        dirnum += 1
        print('%s\t%s\t\t%s' % (time.strftime("%Y/%m/%d %H:%M", time.localtime(os.path.getmtime(name))), '<DIR>', name))
print(filenum, '个文件', fsize, '字节')
print(dirnum, '个目录')
