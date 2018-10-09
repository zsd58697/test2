'''
1.
class Account:
    def __init__(self,id1=0,balance=100,ann=0):
        self.__id=int(id1)
        self.__balance=float(balance)
        self.__ann=float(ann)
        print(self.__id)
    def getMon(self):
        self.Mon=self.__ann/12
        print(self.Mon)
    def winthdraw(self,a):
        self.w=self.__balance-a
    def deposit(self,b):
        self.d=self.w+b
        print(self.d)
    def getMonre(self):
        self.Monre=(self.__ann/12)*self.d
        print(self.Monre)

A=Account(1122,20000,0.045)
A.getMon()
A.winthdraw(2500)
A.deposit(3000)
A.getMonre()
'''

'''
2.
import math
class regularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=int(n)
        self.__side=float(side)
        self.__x=float(x)
        self.__y=float(y)
    def getPerimeter(self):
        self.P=self.__n*self.__side
        print("the duo bian xing perimeter is {}".format(self.P))

    def Area(self):
        self.s=pow(self.__side,2)
        self.t=math.tan(math.pi/self.__n)
        self.a=(self.__n*self.s)/(4*self.t)
        print("the duo bian xing area is {}".format(self.a))
regularPolygon().getPerimeter()
regularPolygon().Area()
regularPolygon(6,4).getPerimeter()
regularPolygon(6,4).Area()
regularPolygon(10,4,5.6,7.8).getPerimeter()
regularPolygon(10,4,5.6,7.8).Area()
'''

'''
3.
class Fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue',):
        self.SLOW=1
        self.MEDIUM=2
        self.FAST=3
        self.__speed=int(speed)
        self.__on=bool(on)
        self.__radius=float(radius)
        self.__color=str(color)
        print("speed is {},on is {} ,radius is {},color is {}".format(self.__speed,self.__on,self.__radius,self.__color))
Fan(3,not False,10,'yellow')
Fan(2,False,5,'blue')
'''
'''
class xd:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.x4=x4
        self.y4=y4
    def k(self):
        self.k1=(self.y2-self.y1)/(self.x2-self.x1)
        self.k2=(self.y4-self.y3)/(self.x4-self.x3)
        if self.k2==self.k1:
            print("no have jiao dian")
        else:
            
'''

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def isSolvable(self):
        self.m=((self.__a*self.__d)-(self.__b*self.__c))
        if self.m!=0:
            return True
        else:
            print("fang cheng wu jie")
    def getX(self):
        self.x=((self.__e*self.__d)-(self.__b*self.__f))/((self.__a*self.__d)-(self.__b*self.__c))
        print(self.x)
    def getY(self):
        self.y=((self.__a*self.__f)-(self.__e*self.__c))/((self.__a*self.__d)-(self.__b*self.__c))
        print(self.y)
A=LinearEquation(3,4,2,3,1,1)
A.isSolvable()
A.getX()
A.getY()







































