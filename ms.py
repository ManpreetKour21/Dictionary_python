# / //

# a=2
# b=4
# c=a/b
# print(c)

# a=4
# a=2
# print(a)


def Divide(D,E):
    R = D
    i = 0
    while R >= E:
        
        R = R - E
        # i += 1
        # print(i)
    return R

D = int(input("enter the number..."))
E = int(input("enter the number.."))
print("Quotient : ",Divide(D,E))



         