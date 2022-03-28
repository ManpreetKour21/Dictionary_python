# my_dict = {
# 'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# n=[]
# for i in my_dict:
#    if my_dict[i]>50:
#       p=my_dict[i]
#       n.append(p)
# print(n)




# my_dict = {
# 'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# n=[]
# for i in my_dict:
#    if my_dict[i]>50:
#       p=my_dict[i]
#       n.append(p)
# print(n)


# my_dict= {'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# n=[]
# for i in my_dict:
#    if my_dict[i]>50:
#       p=my_dict[i]
#       n.append(p)
# print(n)















# my_dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# n=[]
# for i in my_dict:
# 	if my_dict[i]>50:
# 		a=my_dict[i]
# 		n.append(a)
# print(n)


from heapq import nlargest
my_dict = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}
 
print("Initial Dictionary:")
print(my_dict, "\n")
 
ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for val in ThreeHighest:
    print(val, ":", my_dict.get(val))