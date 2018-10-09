# _*_conding:utf8-
from __future__ import print_function
'''
1.
s=0
def getPentagonalNumber(n):
    global s
    for i in range(1,n):
        i=int(i)
        i=(3*i*i-i)/2
        s=s+1
        print(str(i)+' ',end=' ')
        if s==10:
            print()
            s=0
getPentagonalNumber(100)
'''

'''
2.
a=0
A=eval(raw_input("enter a number:"))
def sumDifits(n):
    global A,a
    while A!=0:
        a=a+A%10
        A=A/10
    print("zhe ge shu d zi shen he shi:{}".format(a))
sumDifits(A)
'''

'''
3.
a,b,c=eval(raw_input("enter three number:"))
def displaySortedNumbers(num1,num2,num3):
    global a,b,c
    if a>b:
        a=a
    else:
        a,b=b,a
    if a>c:
        a=a
    else:
        a,c=c,a
    if b>c:
        b=b
    else:
        b,c=c,b
    print("the sorted numbers:{} {} {}".format(c,b,a))
displaySortedNumbers(a,b,c)
'''

'''
3.2
import math 
a,b,c=eval(raw_input("enter three numbers:"))
def displaySortedNumbers(num1,num2,num3):
    global a,b,c
    z=[a,b,c]
    z.sort()
    print("the sorted numbers:{}".format(z))
displaySortedNumbers(a,b,c)
'''

'''
5.
a,b=raw_input("enter begin number and stop number :").split(',')
c= eval(raw_input("enter a number:"))
s=0
def printchars(chr1,chr2,numberperline):
    global a,b,c,s
    a=ord(a)+1
    b=ord(b)+1
    for i in range(a,b):
        s=s+1
        i=chr(i)
        print(str(i)+' ',end='')
        if s==c:
            print()
            s=0
printchars(a,b,c)
'''
'''
5.2
a=ord('1')
b=ord('Z')+1
def printchars(chr1,chr2):
    global a,b,s
    s=0
    for i in range(a,b):
        s=s+1
        i=chr(i)
        print(i+' ',end='')
        if s==10:
            print()
            s=0
printchars(a,b)
'''

'''
6.
a,b=eval(raw_input("enter two years:"))
def numberOfDaysInAYear(year1,year2):
    global a,b
    for i in range(a,b+1):
        if ((i%4==0)&(i%100!=0))|(i%400==0):
            print("{} year de day is 366".format(i))
        else:
            print("{} year de day is 365".format(i))
numberOfDaysInAYear(a,b)
'''
'''
7.
import math
x1,y1=eval(raw_input("enter x1 and y1:"))
x2,y2=eval(raw_input("enter x2 and y2:"))
def distance (a,b,c,d):
    global x1,y1,x2,y2
    d=0
    d=math.sqrt(pow((y2-y1),2)+pow((x2-x1),2))
    print(d)
distance(x1,y1,x2,y2)
'''
'''
8.
print("p,pow(2,p)-1")
s=0
for i in range(2,32):
    s=pow(2,i)-1
    print(i,s)
'''
'''
8.2
print("p\t2^p-1:")
def s(a):
    c=0
    for j in range(2,int(sqrt(a)+1)):
            if a%j==0:
                c=0
            else:
                c=1
    return c
print("2\t3")
for i in range(1,32):
    c=pow(2,i)-1
    if(s(c)):
print("%d\t%d"%(i,c))
'''
'''
9.
from time import *
print(ctime(time()))
'''
'''
10.
import random
n1=random.randint(1,6)
n2=random.randint(1,6)
if (n1+n2==2)|(n1+n2==3)|(n1+n2==12):
    print("you rolled is {} + {} ={}\nyou lose".format(n1,n2,n1+n2))
elif (n1+n2==7)|(n1+n2==11):
    print("you rolled is {} + {} = {}\nyou win".format(n1,n2,n1+n2))
else:
    while(1)
    print("you rolled {} + {} = {}\npoint is {}".format(n1,n2,n1+n2,n1+n2))
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    if(n1+n2==7):
        print("you rolled {} + {} = {}\nyou lose".format(n1,n2,n1+n2))
        break
    elif(n1+n2==n1+n2):
        print("you rolled {} + {} = {}\nyou win".format(n1,n2,n1+n2))
        break
    else:
        continue
'''
'''
4.
import math
p=eval(raw_input("the amount invested:"))
a=eval(raw_input("annual interest rate:"))
def f(c,b):
    global p,a
    print("years   future value ")
    for i in range(1,31):
        p=p*pow((1+a/12),12)
        print(i,p)
f(p,a)
'''
'''
10.2
a,b=eval(rinput("Enter one  and two:"))
if(a+b==2)|(a+b==3)|(a+b==12):
    print("You rolled %d+%d=%d"%(a,b,a+b))
    print("You lose")
elif(a+b==7)|(a+b==11):
    print("You rolled %d+%d=%d"%(a,b,a+b))
    print("You win")
else:
    while(1):
        print("You rolled %d+%d=%d"%(a,b,a+b))
        print("print is %d"%(a+b))
        s=a+b
        a,b=eval(input("Enter one  and two:"))
        if(a+b==7):
            print("You rolled %d+%d=%d"%(a,b,a+b))
            print("You lose")
            break
        elif(a+b==s):
            print("You rolled %d+%d=%d"%(a,b,s))
            print("You win")
            break
        else:
           continue
'''
















