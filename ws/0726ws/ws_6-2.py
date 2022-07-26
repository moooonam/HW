grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


a = 0
for i in grain_lst:
    if a < int(i[1]):
        a = int(i[1])
for j in grain_lst:
    if a in j:
        print(j[0]) 
    