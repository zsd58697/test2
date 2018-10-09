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
        self.s=self.__side*self.__side
        self.t=(math.sin(math.pi/self.__n))/(math.cos(math.pi/self.__n))
        self.a=(self.__n*self.s)/4*self.t
        print("the duo bian xing area is {}".format(self.a))
regularPolygon().getPerimeter()
regularPolygon().Area()
regularPolygon(x=6,y=4).getPerimeter()
regularPolygon(x=6,y=4).Area()
regularPolygon(10,4,5.6,7.8).getPerimeter()
regularPolygon(10,4,5.6,7.8).Area()
'''


















