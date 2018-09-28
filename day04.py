'''
a = 10000 
i,s = 0,0
for i in range(10):
    a=a*(1+0.05)
print("10 years later ${}".format(a))
for i in range(4):
    s=s+a
    a=a*(1+0.05)
print("4 years add {}".format(s))
'''
'''
def NB(name1,*,name2='a',name3='a'):
    print(name1,name2,name3)
NB('a',name2='a',name3='a')
'''
'''
import requests
def a(url):
    html =requests.get(url)
    print(html.txt)
a(url='https://github.com/aixiaocha/test/blob/master/day03zy.py')
'''

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
















