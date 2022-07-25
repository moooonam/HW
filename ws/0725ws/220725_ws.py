# 220726 ws
#문제1

def get_dict_avg(dict):
    a = 0
    for i in dict:
        a+=dict[i]

    return a/len(dict)

my_dict= {'python': 80, 'web': 83, 'algorithm': 90, 'django': 89}
print(get_dict_avg(my_dict))


#문제 2
def count_blood(list):
    a=list.count('A')
    b=list.count('B')
    ab=list.count('AB')
    o=list.count('O')

    return {'A':a,'B':b,'O':o,'AB':ab}

print(count_blood(['A','A','A','B','B','B','O','O','O','AB','AB','AB']))
