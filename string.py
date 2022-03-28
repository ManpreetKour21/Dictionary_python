dic={}
string = input("enter the string: ")
i=0
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[j]==string[i]:
            count=count+1
            dic.update({string[i]:count})
        j=j+1
    i=i+1
print(dic)
