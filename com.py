# dict2={n:n*2 for n in range(10)}
# print(dict2)

# dict2={n:n*2 for n in range(10) if n%2==0}
# print(dict2)

dict3={n:(n if n%2==0 else "invalid")for n in range(10)}
print(dict3)