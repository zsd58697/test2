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
4.
money=eval(raw_input("the amount invested:"))
rate=eval(raw_input("annual interest rate:"))
print("Years  Future Value")
for i in (30):
    s=money*rate(1+rate)
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






















