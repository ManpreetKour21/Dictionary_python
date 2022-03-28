from functools import total_ordering


my_dict = {'data1':100,'data2': -54,'data3': 247}
# a=100+-54+247
# print(a)
for values in my_dict:
    values=my_dict.values()
    total=sum(values)
print(total)


