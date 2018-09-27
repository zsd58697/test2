'''
#_*_coding:utf8-
print('222222')
a = raw_input('>>')
print(a)
# python day03.py >test.txt 
# python day03.py <test.txt
'''
'''
a = 'abced'
i=0
while i<len(a):
    print(a[i])
    i=i+1
'''
'''
n =eval(raw_input(":"))
m= n
while n!=0:
    n=eval(raw_input(":"))
    if n>m:
        m=n
print(m)
print(n)
'''
'''
import random
a=random.randint(0,10)
b=eval(raw_input("enter a between 0 and 10 number:"))
if b==a:
    print("you are so smart!")
else:
    while (b!=a):
        if b>a:
            print("big number,again")
            b=eval(raw_input("enter a between 0 and 10 number:"))
        if b<a:
            print("small number,again")
            b=eval(raw_input("enter a between 0 and 10 number:"))
        if b==a:
            print("you are so smart")
'''
'''
sum1 = 0
i=0
while(i<1001):
    sum1=sum1+i
    i=i+1
print(sum1)
'''
'''
s = 0
i = 1
for i in range (1000):
    s=s+i
    if s>10000:
        print(i)
        break
'''
'''
for i in range (10):
    for j in range (1,i+1):
        print ("{}*{}={} ".format(i,j,i*j),end='')
    print("  ")
'''

def fun1(n1,n2,n3):
    print(n1,n2,n3)
    return (n1,n2,n3)
def fun2(n1,n2,n3):
    a=n1*n1
    b=n2*n2
    c=n3*n3
    print(a,b,c)
    return(a,b,c)
def fun3(a,b,c):
    e=(a-b)+(a-c)+(b-c)
    print(e)
a,b,c=fun1(1,2,3)
x,y,z=fun2(a,b,c)
fun3(a,b,c)

























































