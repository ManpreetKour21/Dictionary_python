# from heapq import nlargest
# my_dict = {'A': 67, 'B': 23, 'C': 45,
#            'D': 56, 'E': 12, 'F': 69}
 
# print("Initial Dictionary:")
# print(my_dict, "\n")
 
# ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
 
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
 
# for val in ThreeHighest:
#     print(val, ":", my_dict.get(val))



my_dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# my_dict = {'c':3, 'a':1, 'd':4, 'b':2}
  
# Sorting dictionary
sorted_dict = my_dict.keys()
sorted_dict = sorted(sorted_dict)
  
# Printing sorted dictionary
print("Sorted dictionary using sorted() and keys() is : ")
for key in sorted_dict:
    print(key,':', my_dict[key])


# a={'bijender':45,'deepak':60,'param':20,'anjili':30}
# for i,j in a.items():
#     for j in i:
#         if 









# my_dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# sorted_dict = my_dict.values()
# sorted_dict = sorted(sorted_dict)
  
# # Printing sorted dictionary
# print("Sorted dictionary using sorted() and valuse.() is : ")
# for value in sorted_dict:
#     print(value,':', my_dict[value])




# orted_dict = my_dict.keys()
# sorted_dict = sorted(sorted_dict)
  
# # Printing sorted dictionary
# print("Sorted dictionary using sorted() and keys() is : ")
# for key in sorted_dict:
#     print(key,':', my_dict[key])
# \