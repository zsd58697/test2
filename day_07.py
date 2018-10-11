# _*_coding:utf8-
'''
1.成绩分级
a1=raw_input("enter a number xiao yu 100:")
a=a1.split()
best=max(a)
for i in range(len(a)):
    a[i]=int(a[i])
    best=int(best)
    if a[i]>=(best-10):
        print("student {} is {} and grade is A".format(i,a[i]))

    elif a[i]>=(best-20):
        print("student {} is {} and grade is B".format(i,a[i]))
    elif a[i]>=(best-30):
        print("student {} is {} and grade is C".format(i,a[i]))
    elif a[i]>=(best-40):
        print("student {} is {} and grade is D".format(i,a[i]))
    else:
        print("student {} is {} and grade is F".format(i,a[i]))
'''
'''
2.输出降序和翻转
a1=input("enter some number:")
a=a1.split()
a.sort(reverse=True)
b=a1.split()
b.reverse()
print("jiang xu shu chu shi :{}".format(a))
print("ni xu shu chu shi :{}".format(b))
'''

'''
3.计数
a1=raw_input("enter some numbers :")
a=a1.split()
s1=set(a)
s1=list(s1)
print(s1)
s={}
print(a)
for i in range(len(a)):
    s[i]=a.count(a[i])
    print("{} occurs {} times".format(a[i],s[i])

'''
'''
3.2
a1=raw_input("enter some numbers :")
s={}
class ep3:
    def __init__(self,a,s):
        self.a=a.split()
        self.s=s
    def js(self):
        for i in self.a:
            self.s[i]=(self.a).count(i)
        #self.sc()
    def sc(self):
        for i in self.s:
            print("{} occurs {} times".format(i,self.s[i]))
A=ep3(a1,s)
#A.js()
A.sc()

'''
'''
4.计算平均分个数
a1=raw_input("enter some occurs:")
a=a1.split()
s=0
s1=0
s2=0
for i in range(len(a)):
    a[i]=int(a[i])
    s=s+a[i]
print(s/(len(a)))
for i in range(len(a)):
    if (s/(len(a)))>=a[i]:
        s1=s1+1
    else:
        s2=s2+1
print("lower ar have {},high ar have {}".format(s1,s2))
'''
'''
5.计算随机数出现次数
import random
a={}
s={}
b=[]
class ep5:
    def __init__(self,a,s,b):
        self.a=a
        self.s=s
        self.b=b
    def suijishu(self):
        for i in range(1000):
            self.a[i]=random.randint(0,9)
        self.b=(self.a).values()
    def jishu(self):
        for i in self.b:
            self.s[i]=(self.b).count(i)
    def shuchu(self):
        for i in self.s:
            print("{} chu xian de ci shu is {}".format(i,self.s[i]))
A=ep5(a,s,b)
A.suijishu()
A.jishu()
A.shuchu()
'''
'''
6.求最小值的最小下标
def indexSE(b1,c1,d):
    global a,b,c,s1
    for i in range(len(a)):
        if a[i]==b:
            if s1==1:
                print(i)
            else:
                c.append(i)
    print(min(c))
a1=raw_input("enter a shu zi list:")
a=a1.split()
b=min(a)
c=[]
s1=a.count(b)
indexSE(a,s1,c)
'''
'''
8.去重
a1=raw_input("enter some number:")
def eli(lst):
    a=a1.split()
    a=set(a)
    b=list(a)
    print("the distinct numbers ares is {}".format(b))
eli(a1)
'''
'''
9.判断输入的列表是否是降序：
a1=raw_input("enter list:")
def isSorted(lst):
    a=a1.split()
    b=a1.split()
    a.sort()
    print(a)
    print(b)
    if a==b:
        print("the list is already sorted")
    else:
        print("the list is no sorted")
isSorted(a1)
'''
'''
10.冒泡：
a1=raw_input("enter a number list:")
a=a1.split()
for i in range(len(a)):
    for j in range(len(a)-1):
        a[j]=int(a[j])
        if a[j]>a[j+1]:
            a[j]=a[j]
        else:
            a[j],a[j+1]=a[j+1],a[j]
a=list(a)
print(a)
'''











































