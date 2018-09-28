'''
1.
s=0
def getPentagonalNumber(n):
    global s
    for i in range(1,n):
        i=int(i)
        i=(3*i*i-i)/2
        s=s+1
        print(str(i)+' ',end=' ')
        if s==10:
            print()
            s=0
getPentagonalNumber(100)
'''

