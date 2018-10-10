# _*_coding:utf8-
'''
 找男女开房的个数：
file = open('/root/wangan.txt',encoding='utf-8',errors='ignore')
s1=0
s2=0
for i in range(1000000):
    line=file.readline()
    if 'M' in line:
        s2=s2+1
    if 'F' in line:
        s1=s1+1
print("man have {},woman have {}".format(s2,s1))
file.close()
'''

'''
输出邮箱：
file = open('/root/wangan.txt',encoding='utf-8',errors='ignore')
for i in range(1000000):
    line=file.readline()
    if '@' in line:
        print(line)
file.close()
'''


'''
判断社会安全号码是否符合规范：
def pd(q):
    global a
    if len(a)==11:
        if a[0]>='0' and a[0]<='9' and a[1]>='0' and a[1]<='9' and a[2]>='0' and a[2]<='9':
            if a[3]=='-':
                if (a[4]>='0' and a[4]<='9')and (a[5]>='0' and a[5]<='9'):
                    if a[6]=='-':
                        if (a[7]>='0' and a[7]<='9') and (a[8]>='0' and a[8]<='9') and (a[9]>='0' and a[9]<='9') and (a[10]>='0' and a[10]<='9'):
                            print("Valid SSN")
                        else:
                            print("Invalid SSN")
                    else:
                        print("Invalid SSN")
                else:
                    print("Invalid SSN")
            else:
                print("Invalid SSN")
        else:
            print("Invalid SSN")
    else:
        print("Invalid SSN")

a=str(raw_input("enter a string li ru ddd-dd-dddd:"))
pd(a)
'''
'''
2.求 子 串
a=raw_input("enter a string:")
b=raw_input("enter anthor string:")
def find(c,d):
    global a,b
    for i in b:
        if i not in a:
            print("b no a zi chuan")
            break
    else:
        print("b is a zi chuan")

find(a,b)
'''
'''
2.2
a=raw_input("enter a string:")
b=raw_input("enter anthor string:")
if b in a:
    print("b is a zi chuan")
else:
    print("b no a zi chuan")
'''
'''
a=raw_input("enter password:")
class ep3:
    def __init__(self,a):
        self.a=a
    def pd(self):
        if len(self.a)>=8:
            return self.a
        else:
            print("invalid password ,chang du bu gou")
    def pd2(self):
        a=self.pd()
        b = a.isalnum()
        if( b==True):
            return a
        else:
            print("invalid password ,no have zi mu or no have shu")
    def pd3(self):
        a=self.pd2()
        s=0
        for i in range(len(a)+1):
            if a[i]>='0'and a[i]<='9':
                s=s+1
        if s>2:
            print("true")
        else:
            print("invalid password")
A=ep3(a)
A.pd3()

'''
'''
3.判断password
def A(n):
    global s,a
    s=0
    if len(a)>=8:
        if (a.isalnum() == True):
            for i in a:
                if (i>='0' and i<='9'):
                    s=s+1
            if s>=2:
                print("valid password")
            else:
                print("invalid password")
        else:
            print("invalid password")
    else:
        print("invalid password")
a=raw_input("enter a password:")
A(a)
'''
'''
4.统计字母个数
def countletters(s1):
    global a,s
    s=0
    for i in a:
        if i>='a' and i<='z':
            s=s+1
    print(s)
a=raw_input("enter a string:")
countletters(a)
'''
def getNumber(u):
    global a
    for i in a:
        if (i=='a' or i=='A'or i=='b'or i=='B'or i=='c'or i=='C'):
            i='2'
        if (i=='d' or i=='D'or i=='e'or i=='E'or i=='f'or i=='F'):
            i='3'
        if (i=='g' or i=='G'or i=='h'or i=='H'or i=='i'or i=='I'):
            i='4'
        if (i=='j' or i=='J'or i=='k'or i=='K'or i=='l'or i=='L'):
            i='5'
        if (i=='m' or i=='M'or i=='n'or i=='N'or i=='o'or i=='O'):
            i='6'
        if (i=='q' or i=='Q'or i=='r'or i=='R'or i=='s'or i=='S' or i=='p' or i=='P'):
            i='7'
        if (i=='t' or i=='T'or i=='u'or i=='U'or i=='v'or i=='v'):
            i='8'
        if (i=='w' or i=='W'or i=='x'or i=='X'or i=='y'or i=='Y' or i=='z'or i=='Z'):
            i='9'
        print (i,end='')
    print()
a=input("enter a telephone number:")
getNumber(a)















































