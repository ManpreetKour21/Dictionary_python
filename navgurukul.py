Dic= {1: 'NAVGURUKUL',2: 'IN',3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
for key ,value in Dic.items():
    del Dic[3]['A']
    break
print(Dic)