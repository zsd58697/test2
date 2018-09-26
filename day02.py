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
a = 'welcome'
b = ' to'
c = ' python'
print(''.join((a,b,c)))
'''
name = eval (raw_input("enter a name:"))
b= ' a handsome boy '
print(''.join((name,b)))














