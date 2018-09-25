'''
1.
celsius=float(raw_input("enter a degree in celsius :"))
fahrenheit = (9/5.0)*celsius+32
print(" {} celsius is {} fahrenheit".format(celsius,fahrenheit))
'''
'''
2.
radius = float (raw_input("enter the radius:"))
length = float (raw_input("enter the length:"))
area = radius * radius * 3.1415
volume = area * length
print("the area is {},the volume is {}".format(area,volume))
'''
'''
3.
feet = float (raw_input("enter a value for feet:"))
meters= 0.305*feet
print("{} feet is {} meters".format(feet,meters))
'''
'''
4.
water,init_temp,final_temp = eval (raw_input("enter the amount of water in kilograms and initinal temperature and final temperature: "))
Q = water * (final_temp - init_temp) * 4184
print("The energy needed is {}".format(Q))
'''
'''
5.
balance,rate = eval(raw_input("enter balance and interest rate:"))
lx = balance * (rate/1200)
print("the interest is {}".format(lx))
'''
'''
6.
v0,v1,t = eval(raw_input("enter v0,v1,t:"))
a=(v1-v0)/t
print("the average acceleration is {}".format(a))
'''
'''
7.
a = eval(raw_input("enter the monthly aumount:"))
i =((((((a*1.00417)+a)*1.00417+a)*1.00417+a)*1.00417+a)*1.00417+100)*1.00417
print("after the sixth month,the accout value is {}".format(i))
'''
'''
8.
number = eval (raw_input("enter a number between 0 and 1000:"))
a = number%10
d = number/10
b = d%10
c = d/10
e = a+b+c
print("The sum of digits is {}".format(e))
'''












































