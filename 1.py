A=eval(raw_input("enter di yi nian xue fei:"))
for i in range(11):
    A=A*(1.05)
A1=A
for i in range(15):
    A1=A1+A*(1.05)
print("enter 10 years after xue fei : {} and sum {}".format(A,A1))
