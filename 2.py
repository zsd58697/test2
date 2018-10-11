class check:
    def __init__(self,a):
        self.a = a.split()
        self.b = {}
    def checks(self):
        for i in self.a:
            if i not in self.b:
                self.b[i] = 1
            else:
                self.b[i] = self.b[i] + 1
        self.printnum()
    def printnum(self):
        for i in self.b:
            print ("{} occurs {} times".format(i,self.b[i]))
a = raw_input("Enter integers between 1 and 100 :")
check(a).checks()
