# _*_ conding:utf8-
'''
1.
class sushu:
    def __init__(self):
        self.a=eval(raw_input("enter a number :"))
    def fuc(self):
        for i in range (2,self.a):
            if (self.a%i)==0:
                print("{} bu shi su shu".format(self.a))
                break
        else:
            print("{} shi su shu".format(self.a))
sushu().fuc()
'''
'''
class ep1:
    def __init__(self):
        self.a=eval(raw_input("enter a number:"))
    def fuc(self):
        if self.a%2==0:
            print("ou")
        else:
            print("ji")
ep1().fuc()
'''
'''
import math
class ep2:
    def __init__(self):
        self.num=10
    def num_2(self):
        self.num = self.num**2
    def num_3(self):
        self.num=pow(self.num,3)
        print(self.num)
ep2()
a.num_2()
a.num_3()
'''
'''
import math
class ep2:
    def __init__(self,num):
        self.num=num
    def num_2(self,b):
        self.num = self.num**2
        print self.num
        print(b)
    def num_3(self):
        self.num=pow(self.num,3)
        print(self.num)
a=ep2(num=9)
a.num_2('num2 very handsome')
a.num_3()
'''
'''
def B(func):
    def warp(*args,**kwargs):
        print("123")
        func()
    return warp
@B
def A():
    print("456")
A()
'''
'''
def B(func):
    def warp(*args,**kwargs):
        print("123")
        func(*args,**kwargs)
    return warp
@B
def A(name,name2):
    print("456"+name+name2)
A("nihao","nihao2")
'''
'''
class mayun:
    def __init__(self):
        self.caichan = 1000
    def show(self):
        print self.caichan
class huwang(mayun):
    def __init__(self):
        mayun.__init__(self)
        self.huwang=10
    def showhuwang(self):
        print("huwang caichan:{}".format(self.caichan))
huwang().showhuwang()
'''
'''
class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        self.Area=self.width*self.height
        print(self.Area)
    def getPerimeter(self):
        self.Per=2*(self.width+self.height)
        print(self.Per)
rectangle(4,40).getArea()
rectangle(4,40).getPerimeter()
rectangle(3.5,35.7).getArea()
rectangle(3.5,35.7).getPerimeter()
'''


























