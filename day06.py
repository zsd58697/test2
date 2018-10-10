'''
a="http://www.baidu.com?page="
b=" wd=xiaopangzi"
for i in range(100):
    print (a+str(i)+b)
'''

'''
b=[1,2,3,'1',True]
print b 
c=list('123')
print c
'''
'''
a=[1,1,1,1,2,2,2,3]
b=[]
for i in (a):
    if i not in b:
        b.append(i)
print b
'''

'''
a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
a4.sort(key = lambda x:x[2][1])
print a4
'''
a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
a5=sorted(a4,key = lambda x:x[2][1])
print a5


