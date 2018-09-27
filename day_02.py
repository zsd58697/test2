'''
1.
import math
r = eval(raw_input("enter the length from the enter to a vertex :"))
s = 2*r*math.sin(math.pi/5)
Area = (5*s*s)/(4*(math.sin(math.pi/5))/(math.cos(math.pi/5)))
print("the area of the pentagon is {}".format(Area))
'''
'''
2. qiu zhi jing
import math
x1,y1 = eval(raw_input("enter point 1(latitude and longitude) in degrees:"))
x2,y2 = eval(raw_input("enter point 2(latitude and longitude) in degress:"))
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
d =6371.01*(math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y2-y1)))
print("the distance between the two points is {}".format(d))
'''
'''
3.
import math
s = eval(raw_input("enter the side:"))
Area = (5*s*s)/(4*(math.sin(math.pi/5))/(math.cos(math.pi/5)))
print("the area of the pentagon is {}".format(Area))
'''
'''
4.
import math
n = eval(raw_input("enter the number of side:"))
s = eval(raw_input("enter the side:"))
Area = (n*pow(s,2))/(4*(math.sin(math.pi/n))/(math.cos(math.pi/n)))
print("the area of the pentagon is {}".format(Area))
'''
'''
5.
A = eval(raw_input("enter an ASCII code:"))
a = chr(A)
print("the character is {}".format(a))
'''
'''
6.
name = raw_input("enter empolyee's name :")
hour = eval(raw_input("entet number of hours worked in a week:"))
rate = eval(raw_input("enter hourly pay rate:"))
federal = eval(raw_input("enter federal tax withholding rate:"))
state = eval(raw_input("enter state tax winthholding rate:"))
print("Employee name:{}".format(name))
print("Hours Worked:{}".format(hour))
prinx,y,z = eval(raw_input("enter three zheng shu:"))
t("Pay Rate:${}".format(rate))
print("Cross Pay:${}".format(rate*hour))
print("Dedutions:\n     Federal withholding (20.0%):{}\n      State Winthholding(9.0%):{}\n       Total Deduction:{}".format(hour*rate*federal,hour*rate*state,hour*rate*federal+hour*rate*state))
print("Net Pay:{}".format(hour*rate-hour*rate*state-hour*rate*federal))
'''
'''
7.
x = eval(raw_input("enter an integer:"))
a = x/1000
b = (x/100)%10
c = (x%100)/10
d = x%10
print("the reversed number is {}{}{}{}".format(d,c,b,a))
'''
'''
8.
res=''
for i in "1107155495@qq.com":
    res = res +chr(ord(i)+1)
print(res)
'''
'''
1.
import math
a,b,c = eval (raw_input("enter a,b,c:"))
e=b*b-4*a*c
r1=(-b+math.sqrt(e))/2*a
r2=(-b-math.sqrt(e))/2*a
if e > 0:
    print("The roots are {} and {}".format(r1,r2))
elif e == 0:
    print("The root is {}".format(r1))
else:
    print("The equation has no real roots")
'''
'''
2.
import random
a = random.randint(0,100)
b = random.randint(0,100)
s = a + b
sum_ = eval(raw_input("enter sum:"))
if sum_ == s:
    print("True")
else:
    print("False")
'''
'''
3.
d1 = eval (raw_input("enter today's day:"))
d2 = eval (raw_input("enter the number of days: "))
if d1+d2 <7:
    s = d1+d2
else:
    s = (d2+d1-7)/7
if d1 == 0:
    A ='Sunday'
elif d1 == 1:
    A ='Monday'
elif d1 == 2:
    A =='Tuesday'
elif d1 == 3:
    A ='wednesday'
elif d1 == 4:
    A ='Thursday'
elif d1 == 5:
    A ='Friday'
else :
    A ='Saturday'
if s == 0:
    print("Today is {} and the future day is Sunday ".format(A))
elif s == 1:
    print("Today is {} and the future day is Monday ".format(A))
elif s == 2:
    print("Today is {} and the future day is Tuesday ".format(A))
elif s == 3:
    print("Today is {} and the future day is wednesday".format(A))
elif s == 4:
    print("Today is {} and the future day is Thursday".format(A))
elif s == 5:
    print("Today is {} and the future day is Friday ".format(A))
else :
    print("Today is {} and the future day is Saturday ".format(A))
'''
'''
4.
import math
x,y,z = eval(raw_input("enter three zheng shu:"))
a=[x,y,z]
a.sort()
print(a)

x,y,z = eval(raw_input("enter three zheng shu:"))
if x>y:
    a=x
else:
    a=y
if a>z:
    a=a
else:
    a=z
if x<y:
    b=x
else:
    b=y
if b<z:
    b=b
else:
    b=z
if x>b&x<a:
    print(b,x,a)
elif y>b&y<a:
    print(b,y,a)
elif z>b&z<a:
    print(b,z,a)
'''
x,y,z=eval(raw_input("enter three number:"))
if x>y:
    x=x
else:
    x=y
if x>z:
    x=x
else:
    x=z
if y>z:
    y=y
else:
    y=z
print(z,y,x)
'''
5.
eight1,price1= eval (raw_input("enter wight and price for package:"))
eight2,price2= eval (raw_input("enter wight and price for package:"))
if eight1*price1<eight2*price2:
    print("package 1 has the better price")
else:
    print("package 2  has the better price")
'''
'''
6.
month,year = eval(raw_input("enter month and year:"))
if (year%4 == 0)&(year%100!=0) | (year%400==0):
    if month==2:
        print("{} year two month have 29 days".format(year))
elif(month==1)|(month==3)|(month==5)|(month==7)|(month==8)|(month==10)|(month==12):
    print("{} year {} month have 31 days".format(year,month))
elif(month==2):
    print("{} year two month have 28 days".format(year))
else:
    print("{} year {} month have 30 days".format(year,month))
'''
'''
7.
import random
a=random.randint(0,1)
b=eval(raw_input("enter 0 or 1:"))
if a==b:
    print("True")
else:
    print("Flase")
'''
'''
8.
import random
a=random.randint(0,2)
b=eval(raw_input("scissor(0),rock(1),paper(2):"))
if (a==0)&(b==0):
    print("the comper scissor.you are scissor.It is a draw.")
elif a==0&b==1:
    print("the comper scissor.you are rock.you won")
elif a==0&b==2:
    print("the comper scissor.you are paper.computer won.")
elif a==1&b==1:
    print("the comper rock.you are rock.It is a draw.")
elif a==1&b==0:
    print("the comper rock.you are scissor.computer won.")
elif a==1&b==2:
    print("the comper rock.you are paper.you won.")
elif a==2&b==2:
    print("the comper paper.you are paper.It is a draw.")
elif a==2&b==0:
    print("the comper paper.you are scissor.computer won.")
else:
    print("the comper paper.you are rock.you won.")
'''
'''
11.
a=eval(raw_input("enter a three-digit integer:"))
x=a%10
y=a%100
if x==y:
    print("{} is a palidrome".format(a))
else:
    print("{} is not a palidrome".format(a))
'''
'''
x,y,z=eval(raw_input("enter three edges:"))
if x+y>z:
    print("the perimeter is {}".format(x+y+z))
elif x+z>y:
    print("the perimeter is {}".format(x+y+z))
elif y+z>x:
    print("the perimeter is {}".format(x+y+z))
else:
    print("ERROR")
'''




































