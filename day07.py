# _*_ coding:utf8-

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
        for i in range(len(a)):
            if a[i]>='0'and a[i]<='9':
                s=s+1
            else:
                s=s
        if s>2:
            print("true")
        else:
            print("invalid password")
A=ep3(a)
A.pd3()
'''
'''
反转
a1=raw_input("enter a number:")
a=list(a1)
a.reverse()
print(a)
'''
'''
a1={'1':1,'2':2,'aa':{1,2}}
print a1.keys()
print a1.values()
print a1.items()
for i,j in a1.items():
    print i,j
print a1.get('4','lallal')
print a1.get('1','hahhhh')
print a1.pop('1')
print a1
print a1.popitem()
a1['11']=1
print a1
'''
#path1='/root/a.txt'
path='/root/wangan.txt'
#file_save=open(path1,'a',encoding='utf-8')
with open(path,'r',encoding='utf-8',errors='ignore') as f:
    #while 1:
    line =f.readline().strip('\n').split(',')
    print(line)
        #try:
            #res=line[-2]
            #if '@' in res:
                #file_save.write(res+'\n')
             #   print (res)
        #except Exception as e:
         #   print(e)
            #print(line)
       # finally:
        #    print('over')
















