def largest(n1,n2,n3,n4):
    if (n1>n2) and (n1>n3) and (n1>n4):
        return n1
    elif (n2>n3)and(n2>n4):
        return n2
    elif (n3>n4):
        return n3
    else:
        return n4

a=largest(1,2,3,4)
print(a)