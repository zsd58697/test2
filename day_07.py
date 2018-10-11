a1=raw_input("enter a number xiao yu 100:")
a=a1.split()
print(a)
for i in range(len(a)):
    a[i]=int(a[i])
    if a[i]>=90 and a[i]<=100):
        print("student {} is {} and grade is A".format(i,a[i]))
    
    elif a[i]>=80 and a[i]<=100:
        print("student {} is {} and grade is B".format(i,a[i]))
    elif a[i]>=70 and a[i]<=100:
        print("student {} is {} and grade is C".format(i,a[i]))
    elif a[i]>=60 and a[i]<=100:
        print("student {} is {} and grade is D".format(i,a[i]))
    else:
        print("student {} is {} and grade is F".format(i,a[i]))
    '''
