'''
1.
A = eval(raw_input("enter a number:"))
s1=0
s2=0
i=0
j=0
while A!=0:
    if A>0:
        s1=s1+A
        i=i+1
    elif A<0:
        s2=s2+A
        j=j+1
    A=eval(raw_input("enter a number:"))
a=float((s1+s2)*1.0/(i+j)*1.0)
print("zheng shu have {} ge,fu shu have {} ge, sum is {},aravage is {}".format(i,j,s1+s2,a))
'''
'''
'''
'''

2.
A=eval(raw_input("enter di yi nian xue fei:"))
for i in range(10):
    A1=A*(1.5)
    A=A+A*(1.5)
print("enter 10 years after xue fei : {} and sum {}".format(A1,A))
'''
'''
3.
s=0
for i in range(100,1000):
    if (i%5==0)&(i%6==0):
        s=s+1
        print(str(i)+' ',end='')
    if s==10:
        print()
        s=0
'''
'''
4.
n=0
while(n*n<12000):
    n=n+1
print(n-1)
n1=1000
while(n1*n1*n1>12000):
    n1=n1-1
print(n1)
'''
'''
5.
money = eval(raw_input("loan Amount:"))
year = eval(raw_input("Number of years:"))
i= 0.05
s1=0
s=0
print("Interest Rate  Monthly Payment  Total Payment")
while i<0.08125:
    s1=s1+(money*year*i)
    i=i+(0.00125)
    s=s+(money*i*year)
    print("%.5f %.5f %.5f "%(i,s1,s))
'''
'''
6.
s=0
for i in range(1,50001):
    s=s+(1.0/i)
print(s)
s1=0
f=50001
for i in range(1,50001):
    s1=s1+(1.0/(f-i))
print(s1)
'''
'''
7.
s=0
a=1
b=3
for i in range(1,98):
    s=s+a*1.0/b*1.0
    a=i+2
    b=a+2
print("sum is %.2f"%(s))
'''
'''
8.
import math
n = eval(raw_input("enter a number:"))
s=0
for i in range(n):
    a=pow(-1,i)
    b=2*(i+1)-1
    s=s+(a*1.0/b*1.0)
    p=4*(s)
    print(p)
print(p)
'''
'''
9.


for i in range(1,10001):
    s=0
    for j in range(1,int(i/2+1)):
        if i%j==0:
            s=s+j
    if s==i:
        print(s)
'''
'''
10.
s=0
for i in range(1,8):
    for j in range(i+1,8):
        if i!=j:
            s=s+1
            print("{} {}".format(i,j))
print(s)
'''









































