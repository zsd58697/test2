# _*_ coding:utf8-
import itertools
path1='/root/txt/p1.txt'
mylist=(''.join(x) for x in itertools.product("0123456789",repeat=3))
with open(path1,'a') as f:

    while 1:
        try:
            f.write(next(mylist)+'\n')
            print("写入成功")
        except Exception as e:
            print(e)
            break

