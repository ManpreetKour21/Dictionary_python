# dict1={'M':0,'I':0,'S':0,'P':0}
# A="MISSISSIPP"
# for i in A:
#     if i=='M':
#         dict1['M']=dict1["M"]+1
#     elif i=='I':
#         dict1['I']=dict1['I']+1
#     elif i=='S':
#         dict1['S']=dict1['S']+1
#     elif i=='P':
#         dict1['P']=dict1['P']+1
# print(dict1)




# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# for i in dict_num:
#     count=count+1
#     print(i,end=" ")
#     print(dict_num[i],count)



dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for i in dict1:
    for j in dict1[i]:
        count+=1
print(count)
