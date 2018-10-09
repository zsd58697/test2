a=0
A=eval(input("enter a number:"))
def sumDifits(n):
    global A,a
    while A!=0:
        a=a+A%10
        A=A//10
    print("zhe ge shu d zi shen he shi:{}".format(a))
sumDifits(A)
