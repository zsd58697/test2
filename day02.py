'''
1.yi zhi zuo biao qiu jiao du
x1,y1 = eval(raw_input("enter A :"))
x2,y2 = eval(raw_input("enter B :"))
x3,y3 = eval(raw_input("enter C :"))
import math
a = math.sqrt(pow(x3-x2,2)+pow(y3-y2,2))
b = math.sqrt(pow(x3-x1,2)+pow(y3-y1,2))
c = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
A = math.degrees(math.acos((pow(a,2)-pow(b,2)-pow(c,2))/(-2*b*c)))
B = math.degrees(math.acos((pow(b,2)-pow(c,2)-pow(a,2))/(-2*a*c)))
C = math.degrees(math.acos((pow(c,2)-pow(a,2)-pow(b,2))/(-2*a*b)))
print(A,B,C)
'''
'''
2. jia mi
res=''
for i in "sddf@22":
    res = res + chr(ord(i)+1)
print(res)
'''
'''
3.zi fu chuan xiang jia shu chu
a = 'welcome'
b = ' to'
c = ' python'
print(''.join((a,b,c)))

name = str(raw_input("enter a name:"))
b= ' a handsome boy '
print(name+b)
'''
'''
if 'a' < 'b':
    print("ok")
if 'a' < 'c':
    print("ok1")
'''
'''
3.
ji ou shu
a = eval(raw_input("enetr a number:"))
if int(a%2) == 0:
    print("ou")
else:
    print("ji")
'''
'''
if yu ju
A = str (raw_input("the boy yes or no  handsome:"))
if A == 'yes':
    print("next problem")
    A == str(raw_input("the boy yes or no have mony"))
    if A=='yes':
        print("next problem")
        A == str(raw_input("the boy yes or no have lao po:"))
        if A=='no':
            print("next problem")
            A == str(raw_input("the boy yes or no have house:"))
            if A=='yes':
                print("i want to see see")
            else:
                print("i want to die")
        else:
            print("go out")
    else:
        print("go out")
else:
    print("go out")
'''
'''
sui ji
from numpy import *
for i in range (10):
    random.seed(10)
    print(random.randint(0,10))
'''
'''
4.cai shu
import random
A = eval(raw_input("enter a number between 0 and 10:"))
if A == random.randint(1,10):
    print("smart")
elif A > random.randint(1,10):
    print("so big")
else:
    print("so small")
'''
import random
A = int(random.randint(0,9))
B = int(random.randint(0,9))
print("{} {}".format(A,B))


























































