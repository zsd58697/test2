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
        if k2==k1:
            print("no have jiao dian")
        else:
            #print(k1,k2)
    def b(self):
        self.b1=-(self.k1*self.x1-self.y1)
        self.b2=-(sele.k2*self.x3-self.y3)
    def Yzuobiao(self):
        self.y=(self.b1-(self.k1*self.b2))/(self.k2-self.k1)
    def Xzuobiao(self)
        self.x=(self.y-self.b2)/self.k2
        return x
    def a(self)
        print(x,y)
xd(2,2,0,0,0,2,2,0).k()
xd(2,2,0,0,0,2,2,0).b()
xd(2,2,0,0,0,2,2,0).Yzuobiao()
xd(2,2,0,0,0,2,2,0).Xzuobiao()
xd(2,2,0,0,0,2,2,0).a()

