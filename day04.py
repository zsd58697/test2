a = 10000 
i,s = 0,0
for i in range(10):
    a=a*(1+0.05)
print("10 years later ${}".format(a))
for i in range(4):
    s=s+a
    a=a*(1+0.05)
print("4 years add {}".format(s))
