# 0726 hw_6-1
def de_identify(jumin):
    mylist = []
    c = 1
    for i in jumin:
        if c<7:
            mylist.append(i)
            c+=1
    result = ''.join(mylist)+'*******'
    return result



print(de_identify('12345678912'))   
