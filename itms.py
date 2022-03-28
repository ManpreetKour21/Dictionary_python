


stu={101:'rahul',102:'raj',103:'sonam'}
it=stu.items()
# print(it)
# print(type(it))
# print()

lst=list(it)
print(lst)
print(type(lst))
print()

# print(lst[0])
# print(lst[0][0])
# print(lst[0][1])

for r in lst:
    for c in r:
        print(c)